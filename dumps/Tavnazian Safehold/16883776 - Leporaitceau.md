# 16883776 - Leporaitceau

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 180 bytes                   |
| Total Events     | 7                           |
| References Count | 15                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [171](#event-171)        | 0x0001       |      1 |              1 |
| [173](#event-173)        | 0x0002       |      1 |              1 |
| [174](#event-174)        | 0x0003       |     16 |              3 |
| [65535.1](#event-655351) | 0x0013       |     28 |              6 |
| [180](#event-180)        | 0x002F       |     11 |              5 |
| [181](#event-181)        | 0x003A       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x044D      |        1101 |
|       1 | 0xFFFFB7FD  |  4294948861 |
|       2 | 0xFFFFA82B  |  4294944811 |
|       3 | 0x02BF      |         703 |
|       4 | 0x1400F     |       81935 |
|       5 | 0x163F      |        5695 |
|       6 | 0xFFFF9DBC  |  4294942140 |
|       7 | 0x03B1      |         945 |
|       8 | 0x000D      |          13 |
|       9 | 0x13F5C     |       81756 |
|      10 | 0xFFFFF981  |  4294965633 |
|      11 | 0xFFFF9E59  |  4294942297 |
|      12 | 0x29E1      |       10721 |
|      13 | 0x29E2      |       10722 |
|      14 | 0x29E3      |       10723 |

## String References

- **10721**: I will not rest until the Marquisate has become as grand and as powerful as it was before the Great War!
- **10722**: With the arrival of the airships, the situation in Tavnazia has begun to take a turn for the better.
- **10723**: Once again Vana'diel will hear the roar of the mighty sealion!

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

### Event 171

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

### Event 173

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

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4E 01 40 A0 01  01 37 00 80 01 80 02 80     N.@...7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0003 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Leporaitceau (ID: 16883776/0x0101A040)
  1: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.101*, z=-18.435*, y=-22.485*, direction=61.8°*
  2: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 04 80 05 80  06 80 07 80 32 08 80 1F     7........2...
0020: 00 09 80 0A 80 0B 80 1F  01 1E 41 A0 01 01 00     ..........A.... 
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=81.935*, z=5.695*, y=-25.156*, direction=83.1°*
  1: 0x001C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x001F [0x1F] MOVE_ENTITY: EventEntity moves to X=81.756*, Z=-1.663*, Y=-24.999*
  3: 0x0027 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0029 [0x1E] EventEntity looks at Anteurephiaux (ID: 16883777/0x0101A041) and starts talking
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1E                 .
0030: F0 FF FF 7F 1D 0C 80 23  21 00                    .......#!.      
```

#### Opcodes

```
  0: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=10721*)
    → "I will not rest until the Marquisate has become as grand and as powerful as it was before the Great War!"
  2: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0038 [0x21] END_EVENT
  4: 0x0039 [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                1E F0 FF FF 7F 1D            ......
0040: 0D 80 23 1D 0E 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x003A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=10722*)
    → "With the arrival of the airships, the situation in Tavnazia has begun to take a turn for the better."
  2: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=10723*)
    → "Once again Vana'diel will hear the roar of the mighty sealion!"
  4: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0047 [0x21] END_EVENT
  6: 0x0048 [0x00] END_REQSTACK()
```
