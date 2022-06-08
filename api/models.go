package main

type Compartment struct {
	Level       int     `gorm:"column:clevel" json:"level"`
	Temperature float32 `json:"temperature"`
}

type User struct {
	Uid  string `json:"uid"`
	Name string `json:"name"`
}
