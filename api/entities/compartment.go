package entities

type Compartment struct {
	ID          uint64  `json:"id"`
	Level       int     `json:"level" gorm:"primaryKey" `
	Temperature float32 `json:"temperature"`
}
