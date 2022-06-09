package models

type Compartment struct {
	Level       int     `gorm:"column:clevel;primaryKey" json:"level"`
	Temperature float32 `json:"temperature"`
}

type User struct {
	Uid  string `json:"uid;primaryKey"`
	Name string `json:"name"`
}

type Market struct {
	Name     string `gorm:"column:mname;primaryKey" json:"name"`
	Location string `json:"location"`
}

type Nutrient struct {
	Name string `gorm:"column:nname;primaryKey" json:"name"`
}
