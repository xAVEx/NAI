// TIC TAC TOE by WrzesieÒ & SzczepaÒski

#include <iostream>
#include <time.h>
#include <conio.h>

using namespace std;

    // FUNKCJA DO USTAWIENIA OP”èNIENIA
    void wait(int sekundy)
{
    clock_t end_wait;
    end_wait = clock() + sekundy * CLOCKS_PER_SEC;
    while (clock() < end_wait) {}
}

struct Move {
    int  r, c, score;
};

struct Tictactoe {
    char player, computer, grid[3][3];
    Tictactoe() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                grid[i][j] = ' ';
            }
        }
    }

    // FUNKCJA SPRAWDZAJ•CA WYGRAN•
    bool win() {
        int win_states[8][3] = { {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6} };
        for (int i = 0; i < 8; i++) {
            bool win = true;
            int first_r = win_states[i][0] / 3, first_c = win_states[i][0] % 3;
            for (int j = 0; j < 3; j++) {
                int r = win_states[i][j] / 3, c = win_states[i][j] % 3;
                if (grid[first_r][first_c] == ' ' || grid[first_r][first_c] != grid[r][c]) {
                    win = false;
                }
            }
            if (win)
                return true;
        }
        return false;
    }

    // FUNKCJA SPRAWDZAJ•CA REMIS
    bool tie() {
        if (win())
            return false;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

    // FUNKCJA RUCH”W GRACZA
    void player_move() {
        while (true) {
            cout << "TwÛj ruch wybierz puste pole od 1 do 9 " << endl;
            int cell;
            cin >> cell;
            int r = (cell - 1) / 3, c = (cell - 1) % 3;
            if (cell >= 1 && cell <= 9 && grid[r][c] == ' ') {
                grid[r][c] = player;
                break;
            }
        }
    }

    // FUNKCJA RUCH”W KOMPUTERA
    void computer_move() {
        Move best_move = minimax();
        grid[best_move.r][best_move.c] = computer;
    }

    Move minimax(bool maximizing_player = true) {
        Move best_move;
        if (win()) {
            if (maximizing_player) {
                best_move.score = -1;
            }
            else {
                best_move.score = 1;
            }
            return best_move;
        }
        else if (tie()) {
            best_move.score = 0;
            return best_move;
        }

        best_move.score = maximizing_player ? -2 : 2;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == ' ') {
                    grid[i][j] = maximizing_player ? computer : player;
                    Move board_state = minimax(!maximizing_player);
                    if (maximizing_player) {
                        if (board_state.score > best_move.score) {
                            best_move.score = board_state.score;
                            best_move.r = i;
                            best_move.c = j;
                        }
                    }
                    else {
                        if (board_state.score < best_move.score) {
                            best_move.score = board_state.score;
                            best_move.r = i;
                            best_move.c = j;
                        }
                    }
                    grid[i][j] = ' ';
                }
            }
        }
        return best_move;
    }

    //FUNKCJA GRY
    void play() {
        while (true) {
            cout << "Wybierz czy chcesz graÊ jako O czy jako X" << endl;
            cout << "GrÍ bÍdzie zaczynaÊ X " << endl;
            wait(1);
            cin >> player;
            if (player == 'X' || player == 'O') {
                break;
            }
        }
        computer = player == 'X' ? 'O' : 'X';
        if (player == 'O') {
            computer_move();
        }
        print();
        while (true) {
            player_move();
            print();
            if (win()) {
                cout << "GRACZ WYGRA£!" << endl;
                return;
            }
            else if (tie()) {
                cout << "REMIS!" << endl;
                return;
            }
            cout << "Komputer wykonuje ruch..." << endl;
            wait(1);
            computer_move();
            print();
            if (win()) {
                cout << "KOMPUTER WYGRA£!" << endl;
                return;
            }
            else if (tie()) {
                cout << "REMIS!" << endl;
                return;
            }
        }
    }

    // WIDOK PLANSZY
    void print() {
        cout << endl;
        for (int i = 0; i < 3; i++) {
            if (i) {
                cout << "-----------" << endl;
            }
            for (int j = 0; j < 3; j++) {
                if (j) {
                    cout << "|";
                }
                cout << ' ';
                if (grid[i][j] == ' ') {
                    cout << 3 * i + j + 1;
                }
                else {
                    cout << grid[i][j];
                }
                cout << ' ';
            }
            cout << endl;
        }
        cout << endl;
    }
};

int main() {
    setlocale(LC_ALL, "");

    Tictactoe game;
    game.play();
    cout << "DziÍkujÍ za grÍ. Gra zakoÒczy siÍ za 4 sekundy";
    wait(4);
}