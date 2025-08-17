# 16883777 - Anteurephiaux

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 144 bytes                   |
| Total Events     | 7                           |
| References Count | 10                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [172](#event-172)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     13 |              3 |
| [173](#event-173)        | 0x000F       |      1 |              1 |
| [174](#event-174)        | 0x0010       |     21 |              4 |
| [177](#event-177)        | 0x0025       |     11 |              5 |
| [178](#event-178)        | 0x0030       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x13F36     |       81718 |
|       1 | 0xFFFFF595  |  4294964629 |
|       2 | 0xFFFF9E5F  |  4294942303 |
|       3 | 0x003C      |          60 |
|       4 | 0x04D3      |        1235 |
|       5 | 0xFFFFC049  |  4294950985 |
|       6 | 0xFFFFA8F7  |  4294945015 |
|       7 | 0x03DB      |         987 |
|       8 | 0x29DF      |       10719 |
|       9 | 0x29E0      |       10720 |

## String References

- **10719**: There's nothing to do in this musty old cave. I wanna go outside and play in the meadows!
- **10720**: I've heard lots of neat stories from all the adventurers visiting the safehold. I can't wait until I'm old enough to ditch this smelly cave and go someplace exciting!

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

### Event 172

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       31 00 00 80 01 80  02 80 03 80 31 01 00       1.........1.. 
```

#### Opcodes

```
  0: 0x0002 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=81.718*, Z=-2.667*, Y=-24.993*, Time=60*
  1: 0x000C [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 173

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 21 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 4E 01 41 A0 01 01 37 04  80 05 80 06 80 07 80 1E  N.A...7.........
0020: 40 A0 01 01 00                                    @....           
```

#### Opcodes

```
  0: 0x0010 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Anteurephiaux (ID: 16883777/0x0101A041)
  1: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.235*, z=-16.311*, y=-22.281*, direction=86.7°*
  2: 0x001F [0x1E] EventEntity looks at Leporaitceau (ID: 16883776/0x0101A040) and starts talking
  3: 0x0024 [0x00] END_REQSTACK()
```

### Event 177

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E F0 FF  FF 7F 1D 08 80 23 21 00       ........#!.
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=10719*)
    → "There's nothing to do in this musty old cave. I wanna go outside and play in the meadows!"
  2: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002E [0x21] END_EVENT
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 178

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 1D 09 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=10720*)
    → "I've heard lots of neat stories from all the adventurers visiting the safehold. I can't wait until I'm old enough to ditch this smelly cave and go someplace exciting!"
  2: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0039 [0x21] END_EVENT
  4: 0x003A [0x00] END_REQSTACK()
```
