package entities

type PreparationMethod struct {
	Name string `gorm:"column:method;primaryKey" json:"name"`
}
