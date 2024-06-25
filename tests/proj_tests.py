import pytest
from server import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.mark.parametrize("poke_name", ["ditto", "eevee", "bulbasaur"])
def test_get_pokemon_data(poke_name):
    response = client.get(f'/pokemons/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by id works successfully\n{response.text}\n')

@pytest.mark.parametrize("pokemon_name", ["stantler", "kingdra"])
def test_add_new_pokemon(pokemon_name):
    response = client.post(f'/pokemons/?pokemon_name={pokemon_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by name works successfully\n{response.text}\n')

@pytest.mark.parametrize("pokemon_type", ['grass', 'fire', 'water'])
def test_get_pokemons_by_type(pokemon_type):
    response = client.get(f'/pokemons/by-type/?pokemon_type={pokemon_type}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemons by type works successfully\n{response.text}\n')

@pytest.mark.parametrize("trainer_name", ['Tierno', 'Ash', 'Brock'])
def test_get_pokemons_by_trainer(trainer_name):
    response = client.get(f'/pokemons/by-trainer/?trainer_name={trainer_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemons by trainer works successfully\n{response.text}\n')

@pytest.mark.parametrize("trainer_name, town", [('Mr.xo',"yafa"), ('Ms.X',"yafa")])
def test_add_trainer(trainer_name, town):
    response = client.post(f'/trainers/?trainer_name={trainer_name}&trainer_town={town}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Add pokemon works successfully\n{response.text}\n')

@pytest.mark.parametrize("trainer_name", ['Mr.xo'])
def test_delete_trainer(trainer_name):
    response = client.delete(f'/trainers/?trainer_name={trainer_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Delete pokemon by name works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name, trainer_name", [('Seadra', 'Ms.X'), (('ditto', 'Ms.X'))])
def test_add_pokemon_to_trainer(poke_name, trainer_name):
    response = client.post(f'/trainers/pokemons/?pokemon_name={poke_name}&trainer_name={trainer_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by id works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name, trainer_name", [('ditto', 'Ms.X')])
def test_delete_pokemon_from_trainer(poke_name, trainer_name):
    response = client.put(f'/trainers/pokemons/?pokemon_name={poke_name}&trainer_name={trainer_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by name works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name", ["ditto", "eevee", "bulbasaur"])
def test_get_image(poke_name):
    response = client.get(f'/images/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemons by type works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name", ["kingdra"])
def test_add_image(poke_name):
    response = client.post(f'/images/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemons by trainer works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name, new_image_url", [("kingdra","www.image_url")])
def test_update_image(poke_name, new_image_url):
    response = client.put(f'images/?poke_name={poke_name}&new_image_url={new_image_url}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Add pokemon works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name, trainer_name", [('Seadra', 'Ms.X')])
def test_evolve(poke_name, trainer_name):
    response = client.put(f'/evolve/?poke_name={poke_name}&trainer_name={trainer_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Delete pokemon by name works successfully\n{response.text}\n')

def main():
    test_get_pokemon_data()
    test_add_new_pokemon()
    test_get_pokemons_by_type()
    test_get_pokemons_by_trainer()
    test_add_trainer()
    test_delete_trainer()
    test_add_pokemon_to_trainer()
    test_delete_pokemon_from_trainer()
    test_get_image()
    test_add_image()
    test_update_image()
    test_evolve()


if __name__ == '__main__':
    main()
