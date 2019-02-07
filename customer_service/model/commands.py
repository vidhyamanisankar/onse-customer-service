def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)


def update_customer(surname, customer_id, customer_repository):
    # create update function in customer_repo
    # query to get customer (using id)
    # param: surname
    # update customer.surname
    customer_repository.update_customer(surname, customer_id)
