# 17723522 - Shomo Pochachilo

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 208 bytes                     |
| Total Events     | 7                             |
| References Count | 9                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |     28 |              5 |
| [65535.1](#event-655351) | 0x001D       |     16 |              2 |
| [65535.2](#event-655352) | 0x002D       |      9 |              3 |
| [65535.3](#event-655353) | 0x0036       |      9 |              3 |
| [675](#event-675)        | 0x003F       |     33 |             12 |
| [696](#event-696)        | 0x0060       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFD3E0  |  4294956000 |
|       1 | 0x0A74      |        2676 |
|       2 | 0xFFFFFF39  |  4294967097 |
|       3 | 0x0FE1      |        4065 |
|       4 | 0x0032      |          50 |
|       5 | 0x001E      |          30 |
|       6 | 0x1C7D      |        7293 |
|       7 | 0x1C7E      |        7294 |
|       8 | 0x1C7F      |        7295 |

## String References

- **7293**: Say, you see that little boy crrrying by the fountain?
- **7294**: Maybe you could help him out. I'm no good with kids.
- **7295**: Haha, I saw that. You rrreturned his fishing pole. How nice of you!

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 92 01 F8 FF FF  7F 37 00 80 01 80 02 80   ".......7......
0010: 03 80 79 00 F8 FF FF 7F  02 70 0E 01 00           ..y......p...   
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-11.296*, z=2.676*, y=-0.199*, direction=357.3°*
  3: 0x0012 [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  4: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         66 04 80               f..
0020: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         5E 69 64               ^id
0030: 6C 30 1C 05 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x002D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0032 [0x1C] WAIT(30* ticks)
  2: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   5E 69  64 6C 30 1C 05 80 00           ^idl0.... 
```

#### Opcodes

```
  0: 0x0036 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x003B [0x1C] WAIT(30* ticks)
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 675

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1E                 .
0040: F0 FF FF 7F 6F 70 29 08  82 70 0E 01 02 1D 06 80  ....op)..p......
0050: 23 1D 07 80 23 29 08 82  70 0E 01 03 20 00 21 00  #...#)..p... .!.
```

#### Opcodes

```
  0: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shomo Pochachilo (ID: 17723522/0x010E7082), tag_num=0x02)
  4: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → "Say, you see that little boy crrrying by the fountain?"
  5: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7294*)
    → "Maybe you could help him out. I'm no good with kids."
  7: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0055 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shomo Pochachilo (ID: 17723522/0x010E7082), tag_num=0x03)
  9: 0x005C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005E [0x21] END_EVENT
 11: 0x005F [0x00] END_REQSTACK()
```

### Event 696

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 1E F0 FF FF 7F 6F 70 29  08 82 70 0E 01 02 1D 08  .....op)..p.....
0070: 80 23 29 08 82 70 0E 01  03 20 00 21 00           .#)..p... .!.   
```

#### Opcodes

```
  0: 0x0060 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0066 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0067 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shomo Pochachilo (ID: 17723522/0x010E7082), tag_num=0x02)
  4: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=7295*)
    → "Haha, I saw that. You rrreturned his fishing pole. How nice of you!"
  5: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0072 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shomo Pochachilo (ID: 17723522/0x010E7082), tag_num=0x03)
  7: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x007B [0x21] END_EVENT
  9: 0x007C [0x00] END_REQSTACK()
```
