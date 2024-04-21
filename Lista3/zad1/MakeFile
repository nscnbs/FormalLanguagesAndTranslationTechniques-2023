FF := flex
FFLAGS :=
BB := bison
BFLAGS :=
CXX := g++
CXXFLAGS := -Wall -Wextra -pedantic -std=c++17

all: flex bison
	$(CXX) $(CXXFLAGS) -o calc calc_lexer.cpp calc_parser.cpp

flex:
	$(FF) $(FFLAGS) -o calc_lexer.cpp calc_lexer.lex

bison:
	$(BB) $(BFLAGS) -d -o calc_parser.cpp calc_parser.y

clean:
	rm -f calc_lexer.cpp calc_parser.hpp calc_parser.cpp calc
