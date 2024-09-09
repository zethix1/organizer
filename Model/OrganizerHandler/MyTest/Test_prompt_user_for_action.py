import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError
from Model.OrganizerHandler.OrganizerHandler import IMAGES_DIR,WALLPAPER_DIR

class Test_prompt_user_for_action(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()
    
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_option1(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action("example.jpg")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.jpg", "Choisir une option", 
                [("Dossier wallpaper", WALLPAPER_DIR, f"Fichier déplacé dans {WALLPAPER_DIR}"),
                ("Dossier images", IMAGES_DIR, f"Fichier déplacé dans {IMAGES_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file, mock_move_file, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.jpg", WALLPAPER_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file est bien appelé pour l'option 1
                mock_move_file.assert_called_once_with("example.jpg", WALLPAPER_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que open_file_explorer_and_prompt n'est pas appelé
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_option2(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 2  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action("example.jpg")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.jpg", "Choisir une option", 
                [("Dossier wallpaper", WALLPAPER_DIR, f"Fichier déplacé dans {WALLPAPER_DIR}"),
                ("Dossier images", IMAGES_DIR, f"Fichier déplacé dans {IMAGES_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file, mock_move_file, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.jpg", IMAGES_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file est bien appelé pour l'option 1
                mock_move_file.assert_called_once_with("example.jpg", IMAGES_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que open_file_explorer_and_prompt n'est pas appelé
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_option3(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 3  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action("example.jpg")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.jpg", "Choisir une option", 
                [("Dossier wallpaper", WALLPAPER_DIR, f"Fichier déplacé dans {WALLPAPER_DIR}"),
                ("Dossier images", IMAGES_DIR, f"Fichier déplacé dans {IMAGES_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file, mock_move_file, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.jpg")  # Simuler l'appel de l'action
                
                # Vérifier que move_file est bien appelé pour l'option 1
                mock_open_explorer.assert_called_once_with("example.jpg")
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que open_file_explorer_and_prompt n'est pas appelé
            assert not mock_move_file.called, "move_file should not have been called"