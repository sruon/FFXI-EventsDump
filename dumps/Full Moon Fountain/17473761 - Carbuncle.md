# 17473761 - Carbuncle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 368 bytes                    |
| Total Events     | 10                           |
| References Count | 36                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     16 |              3 |
| [32001](#event-32001)    | 0x0011       |     16 |              3 |
| [65535.1](#event-655351) | 0x0021       |     41 |              6 |
| [65535.2](#event-655352) | 0x004A       |     17 |              5 |
| [65535.3](#event-655353) | 0x005B       |     14 |              4 |
| [65535.4](#event-655354) | 0x0069       |     24 |              6 |
| [65535.5](#event-655355) | 0x0081       |     10 |              2 |
| [65535.6](#event-655356) | 0x008B       |     14 |              4 |
| [65535.7](#event-655357) | 0x0099       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x53326     |      340774 |
|       1 | 0xFFFAD11A  |  4294627610 |
|       2 | 0xB94C      |       47436 |
|       3 | 0x0491      |        1169 |
|       4 | 0x5273B     |      337723 |
|       5 | 0xFFFACBFD  |  4294626301 |
|       6 | 0xB9CD      |       47565 |
|       7 | 0x0C05      |        3077 |
|       8 | 0x005A      |          90 |
|       9 | 0x0198      |         408 |
|      10 | 0x0024      |          36 |
|      11 | 0x53658     |      341592 |
|      12 | 0xFFFAD0F0  |  4294627568 |
|      13 | 0xB972      |       47474 |
|      14 | 0xFFFFFF00  |  4294967040 |
|      15 | 0x53282     |      340610 |
|      16 | 0xFFFAD9D7  |  4294629847 |
|      17 | 0xB929      |       47401 |
|      18 | 0x53348     |      340808 |
|      19 | 0xFFFACD0B  |  4294626571 |
|      20 | 0xB980      |       47488 |
|      21 | 0x5311D     |      340253 |
|      22 | 0xFFFAC9D5  |  4294625749 |
|      23 | 0xB97C      |       47484 |
|      24 | 0x53194     |      340372 |
|      25 | 0xFFFAD304  |  4294628100 |
|      26 | 0xB93A      |       47418 |
|      27 | 0x04AF      |        1199 |
|      28 | 0x0028      |          40 |
|      29 | 0x52E04     |      339460 |
|      30 | 0xFFFABB72  |  4294622066 |
|      31 | 0xBA58      |       47704 |
|      32 | 0x000D      |          13 |
|      33 | 0x53113     |      340243 |
|      34 | 0xFFFADA85  |  4294630021 |
|      35 | 0xB90D      |       47373 |

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=340.774*, z=-339.686*, y=47.436*, direction=102.7°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    92 01 F8 FF FF 7F 37  04 80 05 80 06 80 07 80   ......7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=337.723*, z=-340.995*, y=47.565*, direction=270.4°*
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 41 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1C 08 80 5B 09 80 F8  FF FF 7F F8 FF FF 7F 00   ...[...........
0030: FE FE FE 22 00 80 F8 FF  FF 7F 5B 09 80 F8 FF FF  ..."......[.....
0040: 7F F8 FF FF 7F 70 6F 70  30 00                    .....pop0.      
```

#### Opcodes

```
  0: 0x0021 [0x1C] WAIT(90* ticks)
  1: 0x0024 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=408*
  2: 0x0033 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0035 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
  5: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 0A 80 1F 00 0B            2.....
0050: 80 0C 80 0D 80 1F 01 39  0E 80 00                 .......9...     
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 36* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=341.592*, Z=-339.728*, Y=47.474*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x39] SET_ENTITY_DIRECTION(direction=358.6°*)
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 0A 80 1F 00             2....
0060: 0F 80 10 80 11 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 36* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=340.610*, Z=-337.449*, Y=47.401*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 0A 80 1F 00 12 80           2......
0070: 13 80 14 80 1F 01 1F 00  15 80 16 80 17 80 1F 01  ................
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 36* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=340.808*, Z=-340.725*, Y=47.488*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=340.253*, Z=-341.547*, Y=47.484*
  4: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    37 18 80 19 80 1A 80  1B 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=340.372*, z=-339.196*, y=47.418*, direction=105.4°*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   32 1C 80 1F 00             2....
0090: 1D 80 1E 80 1F 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x008B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=339.460*, Z=-345.230*, Y=47.704*
  2: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             32 20 80 1F 00 21 80           2 ...!.
00A0: 22 80 23 80 1F 01 00                              ".#....         
```

#### Opcodes

```
  0: 0x0099 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=340.243*, Z=-337.275*, Y=47.373*
  2: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A6 [0x00] END_REQSTACK()
```
