package entities

type Nutrient struct {
	Name string `gorm:"column:nname;primaryKey" json:"name"`
}
