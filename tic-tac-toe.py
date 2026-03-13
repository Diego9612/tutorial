from random import choice

class GameState:

   def __init__(self, player_letter):
        self.player = player_letter
        self.cpu = "X" if self.player == "O" else "O"
        self.player_turn = choice((True, False))
 #       if self.player =="0":
           self.cpu ="X"
 #      else:
           self.cpu="O"
        self.positions = {
            "nw": " ",
            "n": " ",
            "ne": " ",
            "w": " ",
            "c": " ",
            "e": " ",
            "sw": " ",
            "s": " ",
            "se": " ",
        }

   def print_grid(self):
        p = self.positions
        print(
            f"""
          {p["nw"]} | {p["n"]} | {p["ne"]}
         ---|---|---
          {p["w"]} | {p["c"]} | {p["e"]}
         ---|---|---
          {p["sw"]} | {p["s"]} | {p["se"]}   
               """
        )

   def get_player_move(self):
      pos_string = ", ".join(self._get_valid_moves())
      while True:
         print("Scrivi la tua mossa. Mosse disponibili: ")
         print(pos_string)
        # 1. Comunicare all'utente gli input validi
        # 2. Controllare sel'input è valido
        # 3. Controllare se la posiziione è vuota prima di
        # scrivere il valoer
        # 4. Se l'input non p valido, continuare a chiedere
        keys = list(self.positions.keys())
        pos_string = ", ".join(keys)
        while True:
            print("Scrivi la tua mossa. Mosse disponibili:")
            print(pos_string)
            user_input = input(">").lower()
            #  if user_input in self.positions and self.positions[user_input] == " ":
            if self.positions.get[user_input] == " ":
                self.positions[user_input] = self.player
                break
            else:
                print("Mossa non valida")
                
   def get_cpu_move(self):
       valid_moves = []
       for pos, val in self.positions.items():
         if val ==" ":
            valid_moves.append(pos)
       # valid_moves ) [pos for pos, val in self.positions.items() if val == " "]
       move = choice(valid_moves)
       self.positions[move] = self.cpu       
      
   def is_end_game(self):  
      # return true if draw
      # return winning if the game is not over
      # return 
      valid_moves = [pos for pos, val in self.positions.items() if val ==" "]
      if not valid_moves:
         return True
      return False
      if not self._get_valid_moves():
         return True
      p = self.positions
      victory_conditions = (
         #lines
         ("nw", "n", "ne"),
         ("w", "c", "e"),
         ("sw", "s", "se"),
         #columns
         ("nw", "", "sw"),
         ("n", "c", "s"),
         ("ne", "e", "se"),
         #diagonals
         ("nw", "c", "se"),
         ("ne", "c", "sw"),
      )
      for combo in victory_conditions:
         if p[combo[0]] == p[combo[1]] == p[combo[2]] and p[combo[3]] != " ":
            return p[combo[0]]
      if(
         (p["nw"] == p["n"] == p["ne"] )
         or
         (p["w"] == p["c"] == p["e"] )
         or
         (p["sw"] == p["s"] == p["se"] )
         or
      )
      
   
   def _get_valid_moves(self):
      valid_moves = []
      for pos, val in self.positions.items():
         if val == " ":
      return[pos for pos, val in self.positions.items():if val ==" "]
   def next_turn(self):
       if self.player_turn:
          self.print_grid()
          self.get_player_move()
       else:
          self.get_cpu_move()

       if self.check_end_game():
         
        self.player_turn = not self.player_turn
        
   def start_game(self):
      while not self.is_end_game():
         self.next_turn()
      self.print_grid()
      print("Gioco concluso")
       
def get_player_letter():
        while True:
            print("Pick yur letter: X or O")
            user_input = input("> ").upper()
            if user_input in ("X", "O"):
                return user_input
            print("input non valido, riprova")
   
       
pl = get_player_letter()
g = GameState(player_letter=pl)
g.print_grid()
g.get_player_move()
g.get_player_letter()
