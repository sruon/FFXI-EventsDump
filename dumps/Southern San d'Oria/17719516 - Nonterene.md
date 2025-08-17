# 17719516 - Nonterene

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 208 bytes                     |
| Total Events     | 5                             |
| References Count | 18                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [503](#event-503)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     35 |              9 |
| [65535.2](#event-655352) | 0x0031       |     13 |              4 |
| [65535.3](#event-655353) | 0x003E       |     36 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE5A43  |  4294859331 |
|       2 | 0xFFFF2F7A  |  4294913914 |
|       3 | 0x0000      |           0 |
|       4 | 0x0DF6      |        3574 |
|       5 | 0xFFFE6266  |  4294861414 |
|       6 | 0xFFFF3815  |  4294916117 |
|       7 | 0xFFFE693D  |  4294863165 |
|       8 | 0xFFFF3E22  |  4294917666 |
|       9 | 0x03E7      |         999 |
|      10 | 0xFFFE7247  |  4294865479 |
|      11 | 0xFFFF45FA  |  4294919674 |
|      12 | 0x03E8      |        1000 |
|      13 | 0xFFFEBA2B  |  4294883883 |
|      14 | 0xFFFF9120  |  4294938912 |
|      15 | 0x07CF      |        1999 |
|      16 | 0x005A      |          90 |
|      17 | 0x00D0      |         208 |

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

### Event 503

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 37 01 80 02  80 03 80 04 80 00         2..7.........  
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-107.965*, z=-53.382*, y=0.000*, direction=314.1°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1F 00                ..
0010: 05 80 06 80 03 80 1F 01  33 01 5A 00 07 80 08 80  ........3.Z.....
0020: 09 80 5A 01 33 00 1F 00  0A 80 0B 80 0C 80 1F 01  ..Z.3...........
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-105.882*, Z=-51.179*, Y=0.000*
  1: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0018 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x001A [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-104.131*, Z=-49.630*, Y=0.999*
  4: 0x0022 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0024 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  6: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.817*, Z=-47.622*, Y=1.000*
  7: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1F 00 0D 80 0E 80 0F  80 1F 01 22 01 00         .........."..  
```

#### Opcodes

```
  0: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-83.413*, Z=-28.384*, Y=1.999*
  1: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x003B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            1C 10                ..
0040: 80 45 11 80 F0 FF FF 7F  F0 FF FF 7F 76 30 30 32  .E..........v002
0050: 03 80 55 11 80 F0 FF FF  7F F0 FF FF 7F 76 30 30  ..U..........v00
0060: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x003E [0x1C] WAIT(90* ticks)
  1: 0x0041 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "v002" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
  2: 0x0052 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "v002" with entities [LocalPlayer, LocalPlayer], work=208*
  3: 0x0061 [0x00] END_REQSTACK()
```
