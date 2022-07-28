package entities

type Market struct {
	Name     string `gorm:"column:mname;primaryKey" json:"name"`
	Location string `json:"location"`
}
