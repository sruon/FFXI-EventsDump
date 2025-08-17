# 17801219 - Tsui Golalapahn

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 184 bytes        |
| Total Events     | 7                |
| References Count | 6                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [61](#event-61)          | 0x001A       |     33 |             12 |
| [166](#event-166)        | 0x003B       |     33 |             12 |
| [313](#event-313)        | 0x005C       |     12 |              3 |
| [315](#event-315)        | 0x0068       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x26FC      |        9980 |
|       3 | 0x26FD      |        9981 |
|       4 | 0x2862      |       10338 |
|       5 | 0x2863      |       10339 |

## String References

- **9980**: So what is all this talk about anotherrr Great Warrr over in the continents?
- **9981**: You just watch. When the flames of battle start raging, it will be the Mithra who save everyone's tails.
- **10338**: Just because something looks interesting doesn't mean you should be putting yourrr paws on it! On what? Why, that flowerrr you touched!
- **10339**: Wherrre did you think this terrible smell was coming from? Don't tell me you didn't notice.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 03 A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).........#...#
0030: 29 08 03 A0 0F 01 02 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsui Golalapahn (ID: 17801219/0x010FA003), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=9980*)
    → "So what is all this talk about anotherrr Great Warrr over in the continents?"
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=9981*)
    → "You just watch. When the flames of battle start raging, it will be the Mithra who save everyone's tails."
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsui Golalapahn (ID: 17801219/0x010FA003), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 166

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 03 A0 0F 01  01 1D 04 80 23 1D 05 80  op).........#...
0050: 23 29 08 03 A0 0F 01 02  20 00 21 00              #)...... .!.    
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsui Golalapahn (ID: 17801219/0x010FA003), tag_num=0x01)
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=10338*)
    → "Just because something looks interesting doesn't mean you should be putting yourrr paws on it! On what? Why, that flowerrr you touched!"
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=10339*)
    → "Wherrre did you think this terrible smell was coming from? Don't tell me you didn't notice."
  7: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Tsui Golalapahn (ID: 17801219/0x010FA003), tag_num=0x02)
  9: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005A [0x21] END_EVENT
 11: 0x005B [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      92 01 F8 FF              ....
0060: FF 7F 80 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x005C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0062 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0067 [0x00] END_REQSTACK()
```

### Event 315

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          92 01 F8 FF FF 7F 80 F8          ........
0070: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0068 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006E [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0073 [0x00] END_REQSTACK()
```
