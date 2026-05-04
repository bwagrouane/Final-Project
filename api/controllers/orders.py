from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from decimal import Decimal

from ..models import orders as model
from ..models.items import Item
from ..models.order_details import OrderDetail


def create(db: Session, request):
    try:
        total_cost = Decimal("0.00")

        new_order = model.Order(
            cost=0
        )

        db.add(new_order)
        db.flush()

        for order_item in request.items:
            item = db.query(Item).filter(Item.id == order_item.item_id).first()

            if not item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Item with id {order_item.item_id} not found"
                )

            if item.quantity < order_item.quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Not enough inventory for item {item.name}"
                )

            item.quantity = item.quantity - order_item.quantity

            total_cost += Decimal(item.price) * order_item.quantity

            new_order_detail = OrderDetail(
                order_id=new_order.id,
                item_id=item.id,
                quantity=order_item.quantity
            )

            db.add(new_order_detail)

        new_order.cost = total_cost

        db.commit()
        db.refresh(new_order)

    except HTTPException:
        db.rollback()
        raise

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_data = request.model_dump(exclude_unset=True)

        item.update(update_data, synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return item.first()


def delete(db: Session, item_id):
    try:
        db_item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not db_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        if db_item.status not in [model.OrderStatus.received, model.OrderStatus.packaging]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Cannot delete an order that is already {db_item.status}")

        db.delete(db_item)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Status of the order
def read_status(db: Session, item_id: int):
    try:
        order = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order ID not found!"
            )
        return order
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
