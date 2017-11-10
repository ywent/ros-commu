// Generated by gencpp from file ssd/ClassifiedObjectArray.msg
// DO NOT EDIT!


#ifndef SSD_MESSAGE_CLASSIFIEDOBJECTARRAY_H
#define SSD_MESSAGE_CLASSIFIEDOBJECTARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <ssd/ClassifiedObject.h>
#include <sensor_msgs/Image.h>

namespace ssd
{
template <class ContainerAllocator>
struct ClassifiedObjectArray_
{
  typedef ClassifiedObjectArray_<ContainerAllocator> Type;

  ClassifiedObjectArray_()
    : objects()
    , image()  {
    }
  ClassifiedObjectArray_(const ContainerAllocator& _alloc)
    : objects(_alloc)
    , image(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::ssd::ClassifiedObject_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::ssd::ClassifiedObject_<ContainerAllocator> >::other >  _objects_type;
  _objects_type objects;

   typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
  _image_type image;




  typedef boost::shared_ptr< ::ssd::ClassifiedObjectArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ssd::ClassifiedObjectArray_<ContainerAllocator> const> ConstPtr;

}; // struct ClassifiedObjectArray_

typedef ::ssd::ClassifiedObjectArray_<std::allocator<void> > ClassifiedObjectArray;

typedef boost::shared_ptr< ::ssd::ClassifiedObjectArray > ClassifiedObjectArrayPtr;
typedef boost::shared_ptr< ::ssd::ClassifiedObjectArray const> ClassifiedObjectArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ssd::ClassifiedObjectArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ssd

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'ssd': ['/home/maurice/catkin_ws/src/ssd/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ssd::ClassifiedObjectArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ssd::ClassifiedObjectArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ssd::ClassifiedObjectArray_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ccc40aeeae1ee53272e491b81bf276de";
  }

  static const char* value(const ::ssd::ClassifiedObjectArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xccc40aeeae1ee532ULL;
  static const uint64_t static_value2 = 0x72e491b81bf276deULL;
};

template<class ContainerAllocator>
struct DataType< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ssd/ClassifiedObjectArray";
  }

  static const char* value(const ::ssd::ClassifiedObjectArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# An array of ClassifiedObject messages\n\
\n\
ClassifiedObject[] objects\n\
\n\
#The classified image\n\
sensor_msgs/Image image\n\
================================================================================\n\
MSG: ssd/ClassifiedObject\n\
# A message representing an object that was classified using caffe.\n\
Header header\n\
\n\
# The certainty of the classification from 0 to 1\n\
float64 score\n\
\n\
# The label attached to this object\n\
string label\n\
\n\
# The bounding box for the classified object\n\
BoundingBox bbox\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: ssd/BoundingBox\n\
# A simple 2d bounding box message\n\
\n\
float64 x_min\n\
float64 y_min\n\
float64 x_size\n\
float64 y_size\n\
================================================================================\n\
MSG: sensor_msgs/Image\n\
# This message contains an uncompressed image\n\
# (0, 0) is at top-left corner of image\n\
#\n\
\n\
Header header        # Header timestamp should be acquisition time of image\n\
                     # Header frame_id should be optical frame of camera\n\
                     # origin of frame should be optical center of cameara\n\
                     # +x should point to the right in the image\n\
                     # +y should point down in the image\n\
                     # +z should point into to plane of the image\n\
                     # If the frame_id here and the frame_id of the CameraInfo\n\
                     # message associated with the image conflict\n\
                     # the behavior is undefined\n\
\n\
uint32 height         # image height, that is, number of rows\n\
uint32 width          # image width, that is, number of columns\n\
\n\
# The legal values for encoding are in file src/image_encodings.cpp\n\
# If you want to standardize a new string format, join\n\
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n\
\n\
string encoding       # Encoding of pixels -- channel meaning, ordering, size\n\
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h\n\
\n\
uint8 is_bigendian    # is this data bigendian?\n\
uint32 step           # Full row length in bytes\n\
uint8[] data          # actual matrix data, size is (step * rows)\n\
";
  }

  static const char* value(const ::ssd::ClassifiedObjectArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.objects);
      stream.next(m.image);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ClassifiedObjectArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ssd::ClassifiedObjectArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ssd::ClassifiedObjectArray_<ContainerAllocator>& v)
  {
    s << indent << "objects[]" << std::endl;
    for (size_t i = 0; i < v.objects.size(); ++i)
    {
      s << indent << "  objects[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ssd::ClassifiedObject_<ContainerAllocator> >::stream(s, indent + "    ", v.objects[i]);
    }
    s << indent << "image: ";
    s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.image);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SSD_MESSAGE_CLASSIFIEDOBJECTARRAY_H
