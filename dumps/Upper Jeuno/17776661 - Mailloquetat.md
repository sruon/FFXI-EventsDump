# 17776661 - Mailloquetat

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 308 bytes             |
| Total Events     | 14                    |
| References Count | 13                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [25](#event-25)          | 0x0001       |     28 |              8 |
| [159](#event-159)        | 0x001D       |      1 |              1 |
| [65535.1](#event-655351) | 0x001E       |     16 |              2 |
| [65535.2](#event-655352) | 0x002E       |     16 |              2 |
| [65535.3](#event-655353) | 0x003E       |      1 |              1 |
| [158](#event-158)        | 0x003F       |     11 |              5 |
| [10151](#event-10151)    | 0x004A       |      7 |              2 |
| [10209](#event-10209)    | 0x0051       |      7 |              2 |
| [10210](#event-10210)    | 0x0058       |      7 |              2 |
| [10211](#event-10211)    | 0x005F       |      7 |              2 |
| [10149](#event-10149)    | 0x0066       |      7 |              2 |
| [65535.4](#event-655354) | 0x006D       |     34 |              8 |
| [65535.5](#event-655355) | 0x008F       |     38 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1BAA      |        7082 |
|       2 | 0x1BB1      |        7089 |
|       3 | 0x0384      |         900 |
|       4 | 0x0001      |           1 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFF1493  |  4294907027 |
|       7 | 0x19526     |      103718 |
|       8 | 0x027F      |         639 |
|       9 | 0xFFFF179E  |  4294907806 |
|      10 | 0x199DD     |      104925 |
|      11 | 0xFFFF1D8D  |  4294909325 |
|      12 | 0x19A08     |      104968 |

## String References

- **7082**: In this temple we pray to Altana. You should pray for forgiveness, too.
- **7089**: You, too, should pray as that faithful one does.

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

### Event 25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7082*)
    → "In this temple we pray to Altana. You should pray for forgiveness, too."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 159

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            66 00                f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        .........tlk0.  
```

#### Opcodes

```
  0: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            66 00                f.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 65 6E 30 00        .........ten0.  
```

#### Opcodes

```
  0: 0x002E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1E                 .
0040: F0 FF FF 7F 1D 02 80 23  21 00                    .......#!.      
```

#### Opcodes

```
  0: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7089*)
    → "You, too, should pray as that faithful one does."
  2: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0048 [0x21] END_EVENT
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 10151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                92 01 F8 FF FF 7F            ......
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x004A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 10209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0051 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 10210

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0058  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0058 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 10211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               92                 .
0060: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x005F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 10149

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0066 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         1C 03 80               ...
0070: 03 2A 10 04 80 32 05 80  1F 00 06 80 07 80 00 80  .*...2..........
0080: 1F 01 03 23 10 04 80 4B  15 40 0F 01 08 80 00     ...#...K.@..... 
```

#### Opcodes

```
  0: 0x006D [0x1C] WAIT(900* ticks)
  1: 0x0070 [0x03] Work_Zone[42] = 1*
  2: 0x0075 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0078 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.269*, Z=103.718*, Y=0.000*
  4: 0x0080 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0082 [0x03] Work_Zone[35] = 1*
  6: 0x0087 [0x4B] UPDATE_ENTITY_YAW(entity=Mailloquetat (ID: 17776661/0x010F4015), yaw=3.5°*)
  7: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               32                 2
0090: 05 80 1F 00 09 80 0A 80  00 80 1F 01 1F 00 0B 80  ................
00A0: 0C 80 00 80 1F 01 4B 15  40 0F 01 08 80 27 05 15  ......K.@....'..
00B0: 40 0F 01 0C 00                                    @....           
```

#### Opcodes

```
  0: 0x008F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0092 [0x1F] MOVE_ENTITY: EventEntity moves to X=-59.490*, Z=104.925*, Y=0.000*
  2: 0x009A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.971*, Z=104.968*, Y=0.000*
  4: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A6 [0x4B] UPDATE_ENTITY_YAW(entity=Mailloquetat (ID: 17776661/0x010F4015), yaw=3.5°*)
  6: 0x00AD [0x27] REQ_SET(priority=0x05, entity_id=Mailloquetat (ID: 17776661/0x010F4015), tag_num=0x0C)
  7: 0x00B4 [0x00] END_REQSTACK()
```
