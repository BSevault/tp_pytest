import pytest
import taches

@pytest.fixture(autouse=True)
def reset_taches():
  taches.taches = []

def test_ajout_tache_valid_input(monkeypatch):
  # Simuler les entrées utilisateur pour ajouter une tâche et quitter ensuite
  inputs = iter(["ajouter", "Faire les courses", "quitter"])

  # Remplacer input() pour chaque appel avec les valeurs de 'inputs'
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Exécuter le fichier de script (qui contient la boucle while)
  taches.run()

  # Vérifier que la tâche a bien été ajoutée dans la liste 'taches'
  assert "Faire les courses" in taches.taches


def test_ajout_tache_invalid_input(monkeypatch, capfd):
  # Simuler les entrées utilisateur pour ajouter une tâche et quitter ensuite
  inputs = iter(["", "quitter"])

  # Remplacer input() pour chaque appel avec les valeurs de 'inputs'
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  # Exécuter le fichier de script (qui contient la boucle while)
  taches.run()

  # Capturer la sortie du terminal
  captured = capfd.readouterr()

  # Vérifier que la sortie contient "Action non reconnue."
  assert "Action non reconnue." in captured.out


def test_voir_tache(monkeypatch, capfd):
  taches.taches = ["test0", "test1", "test2"]

  inputs = iter(["voir", "quitter"])

  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  taches.run()

  assert "test0" in taches.taches
  assert "test1" in taches.taches
  assert "test2" in taches.taches


def test_supprimer_tache_valid_index(monkeypatch):
  taches.taches = ["test0", "test1", "test2"]

  inputs = iter(["supprimer", 2, "quitter"])

  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  taches.run()

  assert "test0" in taches.taches
  assert "test2" in taches.taches
  assert "test1" not in taches.taches


def test_supprimer_tache_invalid_index(monkeypatch, capfd):
  taches.taches = ["test0", "test1", "test2"]

  inputs = iter(["supprimer", 4, "quitter"])

  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  taches.run()

  captured = capfd.readouterr()

  assert "test0" in taches.taches
  assert "test2" in taches.taches
  assert "test1" in taches.taches
  assert "Indice invalide" in captured.out

