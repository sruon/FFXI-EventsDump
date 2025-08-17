# 17604682 - Talking Doll

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Cloister of Storms (ID: 202) |
| Block Size       | 284 bytes                    |
| Total Events     | 11                           |
| References Count | 21                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [32000](#event-32000)    | 0x0027       |      1 |              1 |
| [32001](#event-32001)    | 0x0028       |      1 |              1 |
| [65535.3](#event-655353) | 0x0029       |      1 |              1 |
| [65535.4](#event-655354) | 0x002A       |     54 |             11 |
| [65535.5](#event-655355) | 0x0060       |      1 |              1 |
| [65535.6](#event-655356) | 0x0061       |     18 |              4 |
| [65535.7](#event-655357) | 0x0073       |     12 |              3 |
| [65535.8](#event-655358) | 0x007F       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FC      |         252 |
|       1 | 0x001E      |          30 |
|       2 | 0x0032      |          50 |
|       3 | 0x0001      |           1 |
|       4 | 0x51DC      |       20956 |
|       5 | 0x7511      |       29969 |
|       6 | 0xFFFFB90E  |  4294949134 |
|       7 | 0x0604      |        1540 |
|       8 | 0x0078      |         120 |
|       9 | 0x6625      |       26149 |
|      10 | 0x868C      |       34444 |
|      11 | 0xFFFFB297  |  4294947479 |
|      12 | 0x05CF      |        1487 |
|      13 | 0x5D5F      |       23903 |
|      14 | 0x803D      |       32829 |
|      15 | 0xFFFFB874  |  4294948980 |
|      16 | 0x05C3      |        1475 |
|      17 | 0x571C      |       22300 |
|      18 | 0x774A      |       30538 |
|      19 | 0xFFFFB912  |  4294949138 |
|      20 | 0x05E1      |        1505 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 62 72 75 30   [..........bru0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 62 72 75 30 5E 69   S........bru0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 54 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                92 01 F8 FF FF 7F            ......
0030: 4E 00 4A A0 0C 01 80 4A  A0 0C 01 6C F8 FF FF 7F  N.J....J...l....
0040: 02 80 03 80 33 01 37 04  80 05 80 06 80 07 80 1E  ....3.7.........
0050: F0 FF FF 7F 6F 70 6C F8  FF FF 7F 08 80 08 80 00  ....opl.........
```

#### Opcodes

```
  0: 0x002A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0030 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17604682/0x010CA04A)
  2: 0x0036 [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17604682/0x010CA04A))
  3: 0x003B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  4: 0x0044 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  5: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.956*, z=29.969*, y=-18.162*, direction=135.3°*
  6: 0x004F [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x0054 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0055 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  9: 0x0056 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=120*, fade_time=120*)
 10: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    92 01 F8 FF FF 7F 33  01 37 09 80 0A 80 0B 80   ......3.7......
0070: 0C 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0061 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0067 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0069 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.149*, z=34.444*, y=-19.817*, direction=130.7°*
  3: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          33 01 37 0D 80  0E 80 0F 80 10 80 00        3.7......... 
```

#### Opcodes

```
  0: 0x0073 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0075 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.903*, z=32.829*, y=-18.316*, direction=129.6°*
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               33                 3
0080: 01 37 11 80 12 80 13 80  14 80 00                 .7.........     
```

#### Opcodes

```
  0: 0x007F [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.300*, z=30.538*, y=-18.158*, direction=132.3°*
  2: 0x008A [0x00] END_REQSTACK()
```
