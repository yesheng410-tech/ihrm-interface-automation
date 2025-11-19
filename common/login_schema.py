import jsonschema

success_schema = {
    "type": "object",
    "required": ["success", "code", "message", "data"],
    "properties": {
        "success": {"type": "boolean", "consist": True},
        "code": {"type": "integer", "consist": 10000},
        "message": {"type": "string", "consist": "操作成功"},
        "data": {"type": "string"}
    }
}

error_schema = {
    "type": "object",
    "required": ["success", "code", "message", "data"],
    "properties": {
        "success": {"type": "boolean", "consist": False},
        "code": {"type": "integer", "consist": 20001},
        "message": {"type": "string", "pattern": "用户名或密码错误"},
        "data": {"type": "null", "consist": None}
    }
}


