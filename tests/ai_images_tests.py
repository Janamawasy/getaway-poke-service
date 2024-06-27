import pytest
from server import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.mark.parametrize("poke1_name, poke2_name", [("ditto", "eevee"), ("bulbasaur", "hoothoot")])
def test_generate_fusion_image(poke1_name, poke2_name):
    response = client.post(f'/ai/images/fusion/?poke1_name={poke1_name}&poke2_name={poke2_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'battle image generator works successfully\n{response.text}\n')

@pytest.mark.parametrize("poke_name", ["ditto", "eevee", "bulbasaur", "hoothoot"])
def test_generate_evolution_image(poke_name):
    response = client.post(f'/ai/images/evolve/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'evolution image generator works successfully\n{response.text}\n')

@pytest.mark.parametrize("prompt", [""])
def test_generate_image(prompt):
    response = client.post(f'/ai/images/?prompt={prompt}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'image generator works successfully\n{response.text}\n')

def main():
    test_generate_battle_image()
    test_generate_evolution_image()
    test_generate_image()

if __name__ == '__main__':
    main()
