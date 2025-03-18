from pet_shop import Dog, PetStore
import pytest

def test_add_dog_age():
    """Test that changing a dogs age works"""
    test_dog = Dog("Dog", 60, 10)
    test_dog.set_age(11)
    assert test_dog.get_age() == 11

def test_add_dog_age_protected():
    """Test that changing a dogs age works"""
    test_dog = Dog("Dog", 60, 10)
    with pytest.raises(AttributeError):
        test_dog.__age

def test_pet_store_add_dog_works():
    """Test that adding a dog works"""
    test_dog = Dog("Dog", 60, 10)
    test_pet_store = PetStore([])

    test_pet_store.add_pet(test_dog)

    assert len(test_pet_store.pets_for_sale()) == 1

def test_pet_store_add_dog_works_two_dogs():
    """Test that adding two dogs works"""
    test_dog1 = Dog("Dog 1", 60, 10)
    test_dog2 = Dog("Dog 2", 60, 10)
    test_pet_store = PetStore([])

    test_pet_store.add_pet(test_dog1)
    test_pet_store.add_pet(test_dog2)

    assert len(test_pet_store.pets_for_sale()) == 2

def test_pet_store_too_many_dogs():
    test_dog1 = Dog("Dog 1", 60, 10)
    test_dog2 = Dog("Dog 2", 60, 10)
    test_dog3 = Dog("Dog 3", 60, 10)
    test_dog4 = Dog("Dog 4", 60, 10)
    test_dog5 = Dog("Dog 5", 60, 10)
    test_dog6 = Dog("Dog 6", 60, 10)
    test_dog7 = Dog("Dog 7", 60, 10)
    test_dog8 = Dog("Dog 8", 60, 10)
    test_dog9 = Dog("Dog 9", 60, 10)
    test_dog10 = Dog("Dog 10", 60, 10)

    pet_store = PetStore([test_dog1, test_dog2, test_dog3,
                              test_dog4, test_dog5, test_dog6, test_dog7, test_dog8, test_dog9])
    with pytest.raises(ValueError):
        pet_store.add_pet(test_dog10)
        pet_store.add_pet(test_dog10)