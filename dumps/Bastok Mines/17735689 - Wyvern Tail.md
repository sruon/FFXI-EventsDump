# 17735689 - Wyvern Tail

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 184 bytes              |
| Total Events     | 6                      |
| References Count | 16                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     14 |              4 |
| [18](#event-18)          | 0x0019       |     11 |              5 |
| [245](#event-245)        | 0x0024       |      1 |              1 |
| [65535.2](#event-655352) | 0x0025       |     43 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFECC15  |  4294888469 |
|       1 | 0xFFFFFF8A  |  4294967178 |
|       2 | 0x001F      |          31 |
|       3 | 0x0025      |          37 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF570C  |  4294924044 |
|       6 | 0xFFFFEEE8  |  4294962920 |
|       7 | 0x0000      |           0 |
|       8 | 0x292C      |       10540 |
|       9 | 0x0006      |           6 |
|      10 | 0x0026      |          38 |
|      11 | 0xFFFFB702  |  4294948610 |
|      12 | 0xFFFE1F38  |  4294844216 |
|      13 | 0xFFFFFC19  |  4294966297 |
|      14 | 0x000F      |          15 |
|      15 | 0x0045      |          69 |

## String References

- **10540**: There are two dungeons outside the city of Bastok: The Palborough Mines in North Gustaberg, and the Dangruf Wadi in South Gustaberg.

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-78.827*, z=-0.118*, y=0.031*, direction=3.3°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.252*, Z=-4.376*, Y=0.000*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1E F0 FF FF 7F 1D 08           .......
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=10540*)
    → "There are two dungeons outside the city of Bastok: The Palborough Mines in North Gustaberg, and the Dangruf Wadi in South Gustaberg."
  2: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0022 [0x21] END_EVENT
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 245

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             00                                        .           
```

#### Opcodes

```
  0: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E 88 A0  0E 01 6F 70 1C 09 80 32       .....op...2
0030: 0A 80 1F 00 0B 80 0C 80  0D 80 1F 01 6F 1C 0E 80  ............o...
0040: 66 0F 80 09 A0 0E 01 09  A0 0E 01 73 68 61 30 00  f..........sha0.
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at Unnamed NPC (ID: 17735816/0x010EA088) and starts talking
  1: 0x002A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002C [0x1C] WAIT(6* ticks)
  4: 0x002F [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  5: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.686*, Z=-123.080*, Y=-0.999*
  6: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x003D [0x1C] WAIT(15* ticks)
  9: 0x0040 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Wyvern Tail (ID: 17735689/0x010EA009), Wyvern Tail (ID: 17735689/0x010EA009)], work=69*
 10: 0x004F [0x00] END_REQSTACK()
```
