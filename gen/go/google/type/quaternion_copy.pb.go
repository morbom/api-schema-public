// Code generated by protoc-gen-go-copy. DO NOT EDIT.
// source: google/type/quaternion.proto

package quaternion

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *Quaternion) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *Quaternion:
		x.X = v.GetX()
		x.Y = v.GetY()
		x.Z = v.GetZ()
		x.W = v.GetW()
	default:
		if v, ok := v.(interface{ GetX() float64 }); ok {
			x.X = v.GetX()
		}
		if v, ok := v.(interface{ GetY() float64 }); ok {
			x.Y = v.GetY()
		}
		if v, ok := v.(interface{ GetZ() float64 }); ok {
			x.Z = v.GetZ()
		}
		if v, ok := v.(interface{ GetW() float64 }); ok {
			x.W = v.GetW()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *Quaternion) Proto_ShallowClone() (c *Quaternion) {
	if x != nil {
		c = new(Quaternion)
		c.X = x.X
		c.Y = x.Y
		c.Z = x.Z
		c.W = x.W
	}
	return
}
