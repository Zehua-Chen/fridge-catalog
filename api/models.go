package main

type Compartment struct {
	Level       int `gorm:"column:clevel"`
	Temperature float32
}

type User struct {
	Uid  string `json:"uid"`
	Name string `json:"name"`
}
