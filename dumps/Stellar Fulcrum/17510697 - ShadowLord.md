# 17510697 - ShadowLord

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 264 bytes                 |
| Total Events     | 7                         |
| References Count | 17                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [17](#event-17)          | 0x000D       |     30 |              5 |
| [65535.1](#event-655351) | 0x002B       |     22 |              5 |
| [65535.2](#event-655352) | 0x0041       |     26 |              8 |
| [65535.3](#event-655353) | 0x005B       |     28 |              7 |
| [65535.4](#event-655354) | 0x0077       |     19 |              3 |
| [65535.5](#event-655355) | 0x008A       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x0000      |           0 |
|       2 | 0x12BC6     |       76742 |
|       3 | 0xFFFFDECD  |  4294958797 |
|       4 | 0x0400      |        1024 |
|       5 | 0x0228      |         552 |
|       6 | 0x1235F     |       74591 |
|       7 | 0xF96F      |       63855 |
|       8 | 0xFFFFEE6C  |  4294962796 |
|       9 | 0xF120      |       61728 |
|      10 | 0xFFFFEC0B  |  4294962187 |
|      11 | 0xE482      |       58498 |
|      12 | 0xFFFFEC75  |  4294962293 |
|      13 | 0x0C00      |        3072 |
|      14 | 0x0040      |          64 |
|      15 | 0x0001      |           1 |
|      16 | 0x01F4      |         500 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 30 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 00 80               2..
0010: 22 01 37 01 80 02 80 03  80 04 80 5B 05 80 F0 FF  ".7........[....
0020: FF 7F F0 FF FF 7F 00 FE  FE FE 00                 ...........     
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x0012 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=76.742*, y=-8.499*, direction=90.0°*
  3: 0x001B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=552*
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 22 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   1F 00 01 80 06             .....
0030: 80 03 80 1F 01 22 01 37  01 80 07 80 08 80 04 80  .....".7........
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=74.591*, Y=-8.499*
  1: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0035 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0037 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=63.855*, y=-4.500*, direction=90.0°*
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    33 01 5A 00 01 80 09  80 0A 80 5A 01 33 00 1F   3.Z.......Z.3..
0050: 00 01 80 0B 80 0C 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x0041 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0043 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=0.000*, Z=61.728*, Y=-5.109*
  2: 0x004B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x004D [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  4: 0x004F [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=58.498*, Y=-5.003*
  5: 0x0057 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 28 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   03 00 00 03 7F             .....
0060: 02 00 00 0D 80 05 76 00  39 00 00 07 00 00 0E 80  ......v.9.......
0070: 1C 0F 80 01 60 00 00                              ....`..         
```

#### Opcodes

```
  0: 0x005B [0x03] ExtData[1]->WorkLocal[0] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
  1: 0x0060 [0x02] IF !(ExtData[1]->WorkLocal[0] > 3072*) GOTO 0x0076
  2: 0x0068 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
  3: 0x006B [0x07] ExtData[1]->WorkLocal[0] += 64*
  4: 0x0070 [0x1C] WAIT(1* ticks)
  5: 0x0073 [0x01] GOTO 0x0060
  6: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      5B  05 80 F8 FF FF 7F F8 FF         [........
0080: FF 7F 74 6C 6B 30 1C 10  80 00                    ..tlk0....      
```

#### Opcodes

```
  0: 0x0077 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=552*
  1: 0x0086 [0x1C] WAIT(500* ticks)
  2: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                22 00 37 01 80 0B            ".7...
0090: 80 0C 80 0D 80 00                                 ......          
```

#### Opcodes

```
  0: 0x008A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x008C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=58.498*, y=-5.003*, direction=270.0°*
  2: 0x0095 [0x00] END_REQSTACK()
```
