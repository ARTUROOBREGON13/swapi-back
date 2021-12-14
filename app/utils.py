def generic_model_mutation_process(model, data, id=None, commit=True):
    """ 
    You can use this function to create and save(optional) existing or new instance on the database using Django ORM.
    
    Args:
        model (django.models.Model): The model class of the object to be changed or created.
        data (dict): This dictionary provides the parameters that are to be changed in the object to be saved and returned.
        id (int, optional): This is the primary key which is assigned to a specific object in the database to be modified. Defaults to None.
        commit (bool, optional): This flag defines if the object being modified must be saved on the database or not. Defaults to True.

    Returns:
        django.models.Model: The instance of class model with the changes specified in the data dictionary.
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
