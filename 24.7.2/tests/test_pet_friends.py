from api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()

"""Получение API Ключа"""
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status,result = pf.get_api_key(email,password)

    assert status == 200
    assert 'key' in result

"""Получение списка всех питомцев"""
def test_get_all_pets_with_vbalid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key,filter)

    assert status == 200
    assert len(result['pets']) > 0

"""Добавление нового питомца"""
def test_add_new_pet_with_valid_data(name='ВРКА', animal_type='Лесное чудище',
                                     age='25', pet_photo='images/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

"""Удаление питомца"""
def test_successful_delete_self_pet():

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "ТОР", "Единарог", "6000", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

"""Обновление информации"""
def test_successful_update_self_pet_info(name='Стрекоза', animal_type='Любви', age=36):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:

        raise Exception("Это чужая Псина")

"""Создание питомца без фото"""
def test_successful_create_simple_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    name = "Барсик"
    animal_type = "Кот"
    age = 3
    status, result = pf.create_pet_simple(auth_key['key'], name, animal_type, age)
    assert status == 200
    assert 'id' in result

"""Получение ключа API с недопустимым email"""
def test_get_api_key_with_invalid_email():
    invalid_email = "invalid_email@example.com"
    _, result = pf.get_api_key(invalid_email, valid_password)
    assert 'key' not in result

"""Получение ключа API с недопустимым паролем"""
def test_get_api_key_with_invalid_password():
    invalid_password = "invalid_password"
    _, result = pf.get_api_key(valid_email, invalid_password)
    assert 'key' not in result

"""Получение ключа API недопустимым пользователем"""
def test_get_api_key_for_invalid_user():
    invalid_email = 'invalid_email@example.com'
    invalid_password = 'invalid_password'
    status, result = pf.get_api_key(invalid_email, invalid_password)

    assert status != 200
    assert 'key' not in result

"""Обновление информации не существующего питомца"""
def test_update_nonexistent_pet_info():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = '9999'
    invalid_name = 'Invalid Pet'
    invalid_animal_type = 'Invalid Type'
    invalid_age = 999
    status, _ = pf.update_pet_info(auth_key, invalid_pet_id, invalid_name, invalid_animal_type, invalid_age)

    assert status != 200

"""Обновление информации питомца с неверным идентификатором"""
def test_update_pet_info_with_invalid_pet_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = '9999'
    name = 'Invalid Pet'
    animal_type = 'Invalid Type'
    age = 999
    status, _ = pf.update_pet_info(auth_key, invalid_pet_id, name, animal_type, age)

    assert status != 200

"""Получение списка питомцев с неверным фильтром"""
def test_get_list_of_pets_with_invalid_filter():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_filter = 'invalid_filter'
    status, _ = pf.get_list_of_pets(auth_key, invalid_filter)

    assert status != 200


