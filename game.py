import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
guessed_letters = []
# Número máximo de intentos permitidos
max_mistakes = 5
# Lista para almacenar las letras adivinadas
print("¡Bienvenido al juego de adivinanzas!")
dificultad = input("Antes de empezar... ¿en que dificultad te gustaría jugar?: \n----facil----\n----media----\n----dificil----\nSelección:")
word_displayed = ""
if dificultad == ("facil"):
   for letra in secret_word:
      if letra not in "aeiou":
         word_displayed += "-"
      else:
         word_displayed += letra
         guessed_letters.append(letra)
elif dificultad == ("media"):
   word_displayed += secret_word[0]
   guessed_letters.append(secret_word[0])
   for letra in range (1, len(secret_word) - 2):
         word_displayed += "_"
   word_displayed += secret_word[len(secret_word) - 1]
   guessed_letters.append(secret_word[len(secret_word) - 1])
else:
      word_displayed = "_" * len(secret_word)



print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while max_mistakes>0:
 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()
 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
    print("Ya has intentado con esa letra. Intenta con otra.")
    continue
 # Agregar la letra a la lista de letras adivinadas
#Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique
#el cambio.
 guessed_letters.append(letter)
 # Verificar si la letra está en la palabra secreta
 if letter in secret_word and letter!="":
    print("¡Bien hecho! La letra está en la palabra.")
 else:
    print("Lo siento, la letra no está en la palabra.")
    max_mistakes = max_mistakes - 1
 # Mostrar la palabra parcialmente adivinada
 letters = []
 for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
 word_displayed = "".join(letters)
 print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
 if word_displayed == secret_word:
    print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
    break
else:
    print(f"¡Oh no! Has agotado tus fallos.")
    print(f"La palabra secreta era: {secret_word}")
