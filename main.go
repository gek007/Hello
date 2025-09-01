package main

import (
	"errors"
	"fmt"
	"log"
	"math"
	"time"
)

type Person struct {
	Name string
	Age  int
}

type Shape interface {
	Area() float32
}

type Square struct {
	sideLen float32
}

func (s Square) Area() float32 {
	return s.sideLen * s.sideLen
}

type Circle struct {
	radius float32
}

func (c Circle) Area() float32 {
	return float32(math.Pi) * c.radius * c.radius
}

func main() {
	fmt.Println("Hello, World!")
	fmt.Printf("Kostya!")
	fmt.Println("Shilkro000t!")

	const IMTPower = 2
	// var userHeight float64
	// var userKg float64

	// fmt.Println("calculate IMT: ")
	// fmt.Print("insert your height: ")
	// fmt.Scan(&userHeight)

	// fmt.Print("insert your weight: ")
	// fmt.Scan(&userKg)
	// var IMT = userKg / math.Pow(userHeight, IMTPower)
	// fmt.Printf("Ваш индекс массы тела: %.2f\n", IMT)

	var name = "Kostya"
	fmt.Printf("Hello, %s!\n", name)

	var name2 string
	name2 = "Shilkro000t"
	fmt.Printf("Hello, %s!\n", name2)
	message, err := EnterTheClub(25)

	if err != nil {
		log.Println(err)
		return
	}

	fmt.Println(message)

	messages1 := []string{"Hello", "World", "from", "Go"}
	fmt.Printf("%v\n", messages1)

	a := 1
	b := 1

	d := addInt(&a, &b)
	fmt.Printf("%v\n", d)

	ages := map[string]int{
		"Alice": 30,
		"Bob":   25,
	}

	t := time.Now()
	fmt.Println("Current time:", t)

	// Add a new key-value pair
	ages["Charlie"] = 22

	// Access a value
	fmt.Println("Alice's age:", ages["Alice"])

	// Iterate over the map
	for name, age := range ages {
		fmt.Printf("%s is %d years old\n", name, age)
	}

	user := Person{
		Name: "John",
		Age:  30,
	}

	fmt.Printf("User: %v\n", user)

}

func EnterTheClub(age int) (string, error) {
	if age >= 18 && age <= 45 {
		return "Welcome", nil
	}

	return "Access Denied", errors.New("You are not allowed to enter")
}

func addInt(a *int, b *int) int {
	return *a + *b
}
