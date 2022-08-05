// Code generated by protoc-gen-go-copy. DO NOT EDIT.
// source: kentik/label/v202203alpha1/label.proto

package label

import "google.golang.org/protobuf/types/known/timestamppb"

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *Label) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *Label:
		x.Id = v.GetId()
		x.Name = v.GetName()
		x.Description = v.GetDescription()
		x.Color = v.GetColor()
		x.Cdate = v.GetCdate()
		x.Edate = v.GetEdate()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
		if v, ok := v.(interface{ GetName() string }); ok {
			x.Name = v.GetName()
		}
		if v, ok := v.(interface{ GetDescription() string }); ok {
			x.Description = v.GetDescription()
		}
		if v, ok := v.(interface{ GetColor() string }); ok {
			x.Color = v.GetColor()
		}
		if v, ok := v.(interface{ GetCdate() *timestamppb.Timestamp }); ok {
			x.Cdate = v.GetCdate()
		}
		if v, ok := v.(interface{ GetEdate() *timestamppb.Timestamp }); ok {
			x.Edate = v.GetEdate()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *Label) Proto_ShallowClone() (c *Label) {
	if x != nil {
		c = new(Label)
		c.Id = x.Id
		c.Name = x.Name
		c.Description = x.Description
		c.Color = x.Color
		c.Cdate = x.Cdate
		c.Edate = x.Edate
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ListLabelsRequest) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ListLabelsRequest) Proto_ShallowClone() (c *ListLabelsRequest) {
	if x != nil {
		c = new(ListLabelsRequest)
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ListLabelsResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *ListLabelsResponse:
		x.Labels = v.GetLabels()
		x.InvalidCount = v.GetInvalidCount()
	default:
		if v, ok := v.(interface{ GetLabels() []*Label }); ok {
			x.Labels = v.GetLabels()
		}
		if v, ok := v.(interface{ GetInvalidCount() rune }); ok {
			x.InvalidCount = v.GetInvalidCount()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ListLabelsResponse) Proto_ShallowClone() (c *ListLabelsResponse) {
	if x != nil {
		c = new(ListLabelsResponse)
		c.Labels = x.Labels
		c.InvalidCount = x.InvalidCount
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *CreateLabelRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *CreateLabelRequest:
		x.Label = v.GetLabel()
	default:
		if v, ok := v.(interface{ GetLabel() *Label }); ok {
			x.Label = v.GetLabel()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *CreateLabelRequest) Proto_ShallowClone() (c *CreateLabelRequest) {
	if x != nil {
		c = new(CreateLabelRequest)
		c.Label = x.Label
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *CreateLabelResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *CreateLabelResponse:
		x.Label = v.GetLabel()
	default:
		if v, ok := v.(interface{ GetLabel() *Label }); ok {
			x.Label = v.GetLabel()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *CreateLabelResponse) Proto_ShallowClone() (c *CreateLabelResponse) {
	if x != nil {
		c = new(CreateLabelResponse)
		c.Label = x.Label
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *UpdateLabelRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *UpdateLabelRequest:
		x.Label = v.GetLabel()
	default:
		if v, ok := v.(interface{ GetLabel() *Label }); ok {
			x.Label = v.GetLabel()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *UpdateLabelRequest) Proto_ShallowClone() (c *UpdateLabelRequest) {
	if x != nil {
		c = new(UpdateLabelRequest)
		c.Label = x.Label
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *UpdateLabelResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *UpdateLabelResponse:
		x.Label = v.GetLabel()
	default:
		if v, ok := v.(interface{ GetLabel() *Label }); ok {
			x.Label = v.GetLabel()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *UpdateLabelResponse) Proto_ShallowClone() (c *UpdateLabelResponse) {
	if x != nil {
		c = new(UpdateLabelResponse)
		c.Label = x.Label
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *DeleteLabelRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *DeleteLabelRequest:
		x.Id = v.GetId()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *DeleteLabelRequest) Proto_ShallowClone() (c *DeleteLabelRequest) {
	if x != nil {
		c = new(DeleteLabelRequest)
		c.Id = x.Id
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *DeleteLabelResponse) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *DeleteLabelResponse) Proto_ShallowClone() (c *DeleteLabelResponse) {
	if x != nil {
		c = new(DeleteLabelResponse)
	}
	return
}
