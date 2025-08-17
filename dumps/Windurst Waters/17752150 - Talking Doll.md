# 17752150 - Talking Doll

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 180 bytes                 |
| Total Events     | 10                        |
| References Count | 4                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [680](#event-680)        | 0x0001       |      1 |              1 |
| [752](#event-752)        | 0x0002       |      1 |              1 |
| [1173](#event-1173)      | 0x0003       |      7 |              2 |
| [65535.1](#event-655351) | 0x000A       |      5 |              2 |
| [65535.2](#event-655352) | 0x000F       |      5 |              2 |
| [65535.3](#event-655353) | 0x0014       |     25 |              3 |
| [65535.4](#event-655354) | 0x002D       |     25 |              3 |
| [65535.5](#event-655355) | 0x0046       |     16 |              2 |
| [65535.6](#event-655356) | 0x0056       |     22 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0C5D      |        3165 |
|       1 | 0x0032      |          50 |
|       2 | 0x00FC      |         252 |
|       3 | 0x001E      |          30 |

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

### Event 680

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 752

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 1173

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0003 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                B6 00 00 80 00               ..... 
```

#### Opcodes

```
  0: 0x000A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3165*)
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               B6                 .
0010: 00 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=50*)
  1: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B4 00 00 00  4D 65 6D 6F 72 69 61 6E      ....Memorian
0020: 00 00 00 00 00 00 00 00  B5 00 00 00 00           .............   
```

#### Opcodes

```
  0: 0x0014 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Memorian")
  1: 0x0028 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B4 00 00               ...
0030: 00 54 61 6C 6B 69 6E 67  00 00 00 00 00 00 00 00  .Talking........
0040: 00 B5 00 00 00 00                                 ......          
```

#### Opcodes

```
  0: 0x002D [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Talking")
  1: 0x0041 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   5B 02  80 F8 FF FF 7F F8 FF FF        [.........
0050: 7F 62 72 75 30 00                                 .bru0.          
```

#### Opcodes

```
  0: 0x0046 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   53 F8  FF FF 7F F8 FF FF 7F 62        S........b
0060: 72 75 30 5E 69 64 6C 30  1C 03 80 00              ru0^idl0....    
```

#### Opcodes

```
  0: 0x0056 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x0063 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0068 [0x1C] WAIT(30* ticks)
  3: 0x006B [0x00] END_REQSTACK()
```
