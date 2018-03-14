// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: question.proto

#ifndef PROTOBUF_question_2eproto__INCLUDED
#define PROTOBUF_question_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace protobuf_question_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[2];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
void InitDefaultsQuestionRequestImpl();
void InitDefaultsQuestionRequest();
void InitDefaultsQuestionResponseImpl();
void InitDefaultsQuestionResponse();
inline void InitDefaults() {
  InitDefaultsQuestionRequest();
  InitDefaultsQuestionResponse();
}
}  // namespace protobuf_question_2eproto
class QuestionRequest;
class QuestionRequestDefaultTypeInternal;
extern QuestionRequestDefaultTypeInternal _QuestionRequest_default_instance_;
class QuestionResponse;
class QuestionResponseDefaultTypeInternal;
extern QuestionResponseDefaultTypeInternal _QuestionResponse_default_instance_;

// ===================================================================

class QuestionRequest : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:QuestionRequest) */ {
 public:
  QuestionRequest();
  virtual ~QuestionRequest();

  QuestionRequest(const QuestionRequest& from);

  inline QuestionRequest& operator=(const QuestionRequest& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  QuestionRequest(QuestionRequest&& from) noexcept
    : QuestionRequest() {
    *this = ::std::move(from);
  }

  inline QuestionRequest& operator=(QuestionRequest&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const QuestionRequest& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const QuestionRequest* internal_default_instance() {
    return reinterpret_cast<const QuestionRequest*>(
               &_QuestionRequest_default_instance_);
  }
  static PROTOBUF_CONSTEXPR int const kIndexInFileMessages =
    0;

  void Swap(QuestionRequest* other);
  friend void swap(QuestionRequest& a, QuestionRequest& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline QuestionRequest* New() const PROTOBUF_FINAL { return New(NULL); }

  QuestionRequest* New(::google::protobuf::Arena* arena) const PROTOBUF_FINAL;
  void CopyFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void MergeFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void CopyFrom(const QuestionRequest& from);
  void MergeFrom(const QuestionRequest& from);
  void Clear() PROTOBUF_FINAL;
  bool IsInitialized() const PROTOBUF_FINAL;

  size_t ByteSizeLong() const PROTOBUF_FINAL;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) PROTOBUF_FINAL;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const PROTOBUF_FINAL;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const PROTOBUF_FINAL;
  int GetCachedSize() const PROTOBUF_FINAL { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const PROTOBUF_FINAL;
  void InternalSwap(QuestionRequest* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const PROTOBUF_FINAL;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // string query = 1;
  void clear_query();
  static const int kQueryFieldNumber = 1;
  const ::std::string& query() const;
  void set_query(const ::std::string& value);
  #if LANG_CXX11
  void set_query(::std::string&& value);
  #endif
  void set_query(const char* value);
  void set_query(const char* value, size_t size);
  ::std::string* mutable_query();
  ::std::string* release_query();
  void set_allocated_query(::std::string* query);

  // @@protoc_insertion_point(class_scope:QuestionRequest)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::ArenaStringPtr query_;
  mutable int _cached_size_;
  friend struct ::protobuf_question_2eproto::TableStruct;
  friend void ::protobuf_question_2eproto::InitDefaultsQuestionRequestImpl();
};
// -------------------------------------------------------------------

class QuestionResponse : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:QuestionResponse) */ {
 public:
  QuestionResponse();
  virtual ~QuestionResponse();

  QuestionResponse(const QuestionResponse& from);

  inline QuestionResponse& operator=(const QuestionResponse& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  QuestionResponse(QuestionResponse&& from) noexcept
    : QuestionResponse() {
    *this = ::std::move(from);
  }

  inline QuestionResponse& operator=(QuestionResponse&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const QuestionResponse& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const QuestionResponse* internal_default_instance() {
    return reinterpret_cast<const QuestionResponse*>(
               &_QuestionResponse_default_instance_);
  }
  static PROTOBUF_CONSTEXPR int const kIndexInFileMessages =
    1;

  void Swap(QuestionResponse* other);
  friend void swap(QuestionResponse& a, QuestionResponse& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline QuestionResponse* New() const PROTOBUF_FINAL { return New(NULL); }

  QuestionResponse* New(::google::protobuf::Arena* arena) const PROTOBUF_FINAL;
  void CopyFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void MergeFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void CopyFrom(const QuestionResponse& from);
  void MergeFrom(const QuestionResponse& from);
  void Clear() PROTOBUF_FINAL;
  bool IsInitialized() const PROTOBUF_FINAL;

  size_t ByteSizeLong() const PROTOBUF_FINAL;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) PROTOBUF_FINAL;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const PROTOBUF_FINAL;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const PROTOBUF_FINAL;
  int GetCachedSize() const PROTOBUF_FINAL { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const PROTOBUF_FINAL;
  void InternalSwap(QuestionResponse* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const PROTOBUF_FINAL;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // string reply = 1;
  void clear_reply();
  static const int kReplyFieldNumber = 1;
  const ::std::string& reply() const;
  void set_reply(const ::std::string& value);
  #if LANG_CXX11
  void set_reply(::std::string&& value);
  #endif
  void set_reply(const char* value);
  void set_reply(const char* value, size_t size);
  ::std::string* mutable_reply();
  ::std::string* release_reply();
  void set_allocated_reply(::std::string* reply);

  // @@protoc_insertion_point(class_scope:QuestionResponse)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::ArenaStringPtr reply_;
  mutable int _cached_size_;
  friend struct ::protobuf_question_2eproto::TableStruct;
  friend void ::protobuf_question_2eproto::InitDefaultsQuestionResponseImpl();
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// QuestionRequest

// string query = 1;
inline void QuestionRequest::clear_query() {
  query_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& QuestionRequest::query() const {
  // @@protoc_insertion_point(field_get:QuestionRequest.query)
  return query_.GetNoArena();
}
inline void QuestionRequest::set_query(const ::std::string& value) {
  
  query_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:QuestionRequest.query)
}
#if LANG_CXX11
inline void QuestionRequest::set_query(::std::string&& value) {
  
  query_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:QuestionRequest.query)
}
#endif
inline void QuestionRequest::set_query(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  
  query_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:QuestionRequest.query)
}
inline void QuestionRequest::set_query(const char* value, size_t size) {
  
  query_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:QuestionRequest.query)
}
inline ::std::string* QuestionRequest::mutable_query() {
  
  // @@protoc_insertion_point(field_mutable:QuestionRequest.query)
  return query_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* QuestionRequest::release_query() {
  // @@protoc_insertion_point(field_release:QuestionRequest.query)
  
  return query_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void QuestionRequest::set_allocated_query(::std::string* query) {
  if (query != NULL) {
    
  } else {
    
  }
  query_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), query);
  // @@protoc_insertion_point(field_set_allocated:QuestionRequest.query)
}

// -------------------------------------------------------------------

// QuestionResponse

// string reply = 1;
inline void QuestionResponse::clear_reply() {
  reply_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& QuestionResponse::reply() const {
  // @@protoc_insertion_point(field_get:QuestionResponse.reply)
  return reply_.GetNoArena();
}
inline void QuestionResponse::set_reply(const ::std::string& value) {
  
  reply_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:QuestionResponse.reply)
}
#if LANG_CXX11
inline void QuestionResponse::set_reply(::std::string&& value) {
  
  reply_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:QuestionResponse.reply)
}
#endif
inline void QuestionResponse::set_reply(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  
  reply_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:QuestionResponse.reply)
}
inline void QuestionResponse::set_reply(const char* value, size_t size) {
  
  reply_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:QuestionResponse.reply)
}
inline ::std::string* QuestionResponse::mutable_reply() {
  
  // @@protoc_insertion_point(field_mutable:QuestionResponse.reply)
  return reply_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* QuestionResponse::release_reply() {
  // @@protoc_insertion_point(field_release:QuestionResponse.reply)
  
  return reply_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void QuestionResponse::set_allocated_reply(::std::string* reply) {
  if (reply != NULL) {
    
  } else {
    
  }
  reply_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), reply);
  // @@protoc_insertion_point(field_set_allocated:QuestionResponse.reply)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)


// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_question_2eproto__INCLUDED
