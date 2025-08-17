# 17735688 - Deadly Spider

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 208 bytes              |
| Total Events     | 7                      |
| References Count | 17                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     14 |              4 |
| [17](#event-17)          | 0x0019       |     30 |              8 |
| [86](#event-86)          | 0x0037       |     16 |              8 |
| [180](#event-180)        | 0x0047       |      1 |              1 |
| [65535.2](#event-655352) | 0x0048       |     23 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE6270  |  4294861424 |
|       1 | 0x3623      |       13859 |
|       2 | 0x0000      |           0 |
|       3 | 0x0454      |        1108 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFE622E  |  4294861358 |
|       6 | 0xFFFFAFC0  |  4294946752 |
|       7 | 0x2928      |       10536 |
|       8 | 0x003C      |          60 |
|       9 | 0x2929      |       10537 |
|      10 | 0x292A      |       10538 |
|      11 | 0x292B      |       10539 |
|      12 | 0xFFFF601A  |  4294926362 |
|      13 | 0x6AE0      |       27360 |
|      14 | 0x0EFF      |        3839 |
|      15 | 0xFFFF6E9D  |  4294930077 |
|      16 | 0x716D      |       29037 |

## String References

- **10536**: Ever since the new president came into office, all manner of public works are falling behind schedule.
- **10537**: He shouldn't meddle with things that don't concern him, and let Chief Cid do his job. Doesn't he realize he's just a figurehead anyway?
- **10538**: What? The stamp hunt? You came all this way for that, huh? Here you go.
- **10539**: You received a stamp!

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-105.872*, z=13.859*, y=0.000*, direction=97.4°*
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
0010: 05 80 06 80 02 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-105.938*, Z=-20.544*, Y=0.000*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1E F0 FF FF 7F 1D 07           .......
0020: 80 23 66 08 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
0030: 30 1D 09 80 23 21 00                              0...#!.         
```

#### Opcodes

```
  0: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=10536*)
    → "Ever since the new president came into office, all manner of public works are falling behind schedule."
  2: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=10537*)
    → "He shouldn't meddle with things that don't concern him, and let Chief Cid do his job. Doesn't he realize he's just a figurehead anyway?"
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x21] END_EVENT
  7: 0x0036 [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      42  1E F0 FF FF 7F 1D 0A 80         B........
0040: 23 48 0B 80 23 21 00                              #H..#!.         
```

#### Opcodes

```
  0: 0x0037 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=10538*)
    → "What? The stamp hunt? You came all this way for that, huh? Here you go."
  3: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0041 [0x48] [System] [10539*]:
    → "You received a stamp!"
  5: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0045 [0x21] END_EVENT
  7: 0x0046 [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 04 80 37 0C 80 0D 80          2..7....
0050: 02 80 0E 80 1F 00 0F 80  10 80 02 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-40.934*, z=27.360*, y=0.000*, direction=337.4°*
  2: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-37.219*, Z=29.037*, Y=0.000*
  3: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005E [0x00] END_REQSTACK()
```
