package main

type Compartment struct {
	Level       int `gorm:"column:clevel"`
	Temperature float32
}
