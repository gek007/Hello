package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Hello, World!")
	fmt.Printf("Kostya!")
	fmt.Printf("Shilkro000t!")

	userHeight := 1.68
	userKg := 92.0
	var IMT = userKg / math.Pow(userHeight, 2)
	fmt.Printf("Ваш индекс массы тела: %.2f\n", IMT)

}
