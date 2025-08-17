# 17830138 - Gregoirellaud

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 260 bytes                 |
| Total Events     | 12                        |
| References Count | 14                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [65535.3](#event-655353) | 0x001F       |     16 |              2 |
| [65535.4](#event-655354) | 0x002F       |     14 |              2 |
| [34](#event-34)          | 0x003D       |      1 |              1 |
| [65535.5](#event-655355) | 0x003E       |     18 |              4 |
| [65535.6](#event-655356) | 0x0050       |     14 |              4 |
| [37](#event-37)          | 0x005E       |      1 |              1 |
| [65535.7](#event-655357) | 0x005F       |     18 |              4 |
| [65535.8](#event-655358) | 0x0071       |     17 |              5 |
| [65535.9](#event-655359) | 0x0082       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00A9      |         169 |
|       1 | 0xFFFFFA0A  |  4294965770 |
|       2 | 0xFFFFE4B5  |  4294960309 |
|       3 | 0x0000      |           0 |
|       4 | 0x03C9      |         969 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFFF972  |  4294965618 |
|       7 | 0xFFFFDF7B  |  4294958971 |
|       8 | 0xFFFFFC17  |  4294966295 |
|       9 | 0xFFFFFF05  |  4294967045 |
|      10 | 0x0C96      |        3222 |
|      11 | 0x0014      |          20 |
|      12 | 0xFFFFF8BC  |  4294965436 |
|      13 | 0xFFFFFF83  |  4294967171 |

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            2F 00                /.
0040: F8 FF FF 7F 37 01 80 02  80 03 80 04 80 22 00 00  ....7........"..
```

#### Opcodes

```
  0: 0x003E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0044 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.526*, z=-6.987*, y=0.000*, direction=85.2°*
  2: 0x004D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 05 80 1F 00 06 80 07  80 03 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.678*, Z=-8.325*, Y=0.000*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               2F                 /
0060: 00 F8 FF FF 7F 37 08 80  09 80 03 80 0A 80 22 00  .....7........".
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0065 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.001*, z=-0.251*, y=0.000*, direction=283.2°*
  2: 0x006E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1C 0B 80 4B F8 FF FF  7F 03 80 6F 76 F8 FF FF   ...K......ov...
0080: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0071 [0x1C] WAIT(20* ticks)
  1: 0x0074 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=0.0°*)
  2: 0x007B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x007C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       37 0C 80 0D 80 03  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0082 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.860*, z=-0.125*, y=0.000*, direction=0.0°*
  1: 0x008B [0x00] END_REQSTACK()
```
