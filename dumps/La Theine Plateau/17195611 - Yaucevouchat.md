# 17195611 - Yaucevouchat

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 72 bytes                    |
| Total Events     | 2                           |
| References Count | 2                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [104](#event-104)     | 0x0001       |     39 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1CF2      |        7410 |

## String References

- **7410**: Well? Find anything?

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 1D 01 80 23 5E 69 64 6C  30 27 64 5C 62 06 01 03  ...#^idl0'd\b...
0020: 2A 64 5C 62 06 01 21 00                           *d\b..!.        
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7410*)
    → "Well? Find anything?"
  2: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0014 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  4: 0x0019 [0x27] REQ_SET(priority=0x64, entity_id=Tayula (ID: 17195612/0x0106625C), tag_num=0x03)
  5: 0x0020 [0x2A] GET_REQ_LEVEL(level=100, entity_id=Tayula (ID: 17195612/0x0106625C))
  6: 0x0026 [0x21] END_EVENT
  7: 0x0027 [0x00] END_REQSTACK()
```
