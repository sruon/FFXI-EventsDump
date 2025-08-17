# 17735700 - Roh Latteh

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 144 bytes              |
| Total Events     | 6                      |
| References Count | 8                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [29](#event-29)          | 0x0001       |     11 |              5 |
| [95](#event-95)          | 0x000C       |     33 |             10 |
| [96](#event-96)          | 0x002D       |      1 |              1 |
| [65535.1](#event-655351) | 0x002E       |     19 |              5 |
| [65535.2](#event-655352) | 0x0041       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x29E1      |       10721 |
|       1 | 0x2A1A      |       10778 |
|       2 | 0x0050      |          80 |
|       3 | 0x2A1B      |       10779 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFFDC49  |  4294958153 |
|       6 | 0xFFFFE2E6  |  4294959846 |
|       7 | 0x1B49      |        6985 |

## String References

- **10721**: My mom's the greatest adventurer ever! Every time she comes back, she brings me lots of neat gifts!
- **10778**: Oh! A prrresent from Mom! Thank you for bringing it!
- **10779**: Wait, don't go yet! Here, could you give this to Mom? Please?

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

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=10721*)
    → "My mom's the greatest adventurer ever! Every time she comes back, she brings me lots of neat gifts!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 95

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 33 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      20 01 42 1E               .B.
0010: F0 FF FF 7F 1D 01 80 23  5B 02 80 F8 FF FF 7F F8  .......#[.......
0020: FF FF 7F 70 61 73 30 1D  03 80 23 21 00           ...pas0...#!.   
```

#### Opcodes

```
  0: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=10778*)
    → "Oh! A prrresent from Mom! Thank you for bringing it!"
  4: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0018 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=80*
  6: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=10779*)
    → "Wait, don't go yet! Here, could you give this to Mom? Please?"
  7: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002B [0x21] END_EVENT
  9: 0x002C [0x00] END_REQSTACK()
```

### Event 96

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 04                2.
0030: 80 1F 00 05 80 06 80 07  80 1F 01 1E 15 A0 0E 01  ................
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.143*, Z=-7.450*, Y=6.985*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x1E] EventEntity looks at Nbu Latteh (ID: 17735701/0x010EA015) and starts talking
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0041 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0046 [0x00] END_REQSTACK()
```
