# 17776672 - Paya-Sabya

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 256 bytes             |
| Total Events     | 9                     |
| References Count | 11                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [80](#event-80)          | 0x0001       |      1 |              1 |
| [79](#event-79)          | 0x0002       |     69 |             15 |
| [23](#event-23)          | 0x0047       |     18 |              6 |
| [94](#event-94)          | 0x0059       |      1 |              1 |
| [29](#event-29)          | 0x005A       |     10 |              4 |
| [65535.1](#event-655351) | 0x0064       |     19 |              3 |
| [65535.2](#event-655352) | 0x0077       |     29 |              3 |
| [65535.3](#event-655353) | 0x0094       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D19      |        7449 |
|       1 | 0x1D1A      |        7450 |
|       2 | 0x1D1B      |        7451 |
|       3 | 0x1D1C      |        7452 |
|       4 | 0x1D1D      |        7453 |
|       5 | 0x1D1E      |        7454 |
|       6 | 0x1D1F      |        7455 |
|       7 | 0x1D3D      |        7485 |
|       8 | 0x0055      |          85 |
|       9 | 0x001E      |          30 |
|      10 | 0x003C      |          60 |

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

### Event 80

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

### Event 79

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 69 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4A 20 40 0F 01 F0  FF FF 7F 2B 20 40 0F 01    J @......+ @..
0010: 00 80 23 4A 21 40 0F 01  20 40 0F 01 2B 21 40 0F  ..#J!@.. @..+!@.
0020: 01 01 80 23 4A 20 40 0F  01 21 40 0F 01 2B 20 40  ...#J @..!@..+ @
0030: 0F 01 02 80 23 2B 21 40  0F 01 03 80 23 2B 20 40  ....#+!@....#+ @
0040: 0F 01 04 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0002 [0x4A] Paya-Sabya (ID: 17776672/0x010F4020) looks at LocalPlayer
  1: 0x000B [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7449*]:
    → "I'm helping Verena and Fickie grow flowers. We water them every-wevery day. I sure hope they bloom soon!"
  2: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0013 [0x4A] Geebeh (ID: 17776673/0x010F4021) looks at Paya-Sabya (ID: 17776672/0x010F4020)
  4: 0x001C [0x2B] Geebeh (ID: 17776673/0x010F4021) [7450*]:
    → "Yeah, right. No way seeds from beastmen'll ever grow."
  5: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0024 [0x4A] Paya-Sabya (ID: 17776672/0x010F4020) looks at Geebeh (ID: 17776673/0x010F4021)
  7: 0x002D [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7451*]:
    → "Nuh-uh! They'll grow!"
  8: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0035 [0x2B] Geebeh (ID: 17776673/0x010F4021) [7452*]:
    → "Yuh-huh! My daddy said that beastmen are gonna start another war! Fickie's the enemy!"
 10: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x003D [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7453*]:
    → "Nuh-uh! Fickie's our friend!"
 12: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0045 [0x21] END_EVENT
 14: 0x0046 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      2B  20 40 0F 01 05 80 23 2B         + @....#+
0050: 20 40 0F 01 06 80 23 21  00                        @....#!.       
```

#### Opcodes

```
  0: 0x0047 [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7454*]:
    → "Fickie told us that when they bloom, it means that people and beasty-weastymen can be friends. I was surprised to hear that, 'specially from a gobbie-wobbie!"
  1: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x004F [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7455*]:
    → "I know they'll bloom. I'm gonna make them."
  3: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0057 [0x21] END_EVENT
  5: 0x0058 [0x00] END_REQSTACK()
```

### Event 94

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0059  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             00                             .      
```

#### Opcodes

```
  0: 0x0059 [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                2B 20 40 0F 01 07            + @...
0060: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x005A [0x2B] Paya-Sabya (ID: 17776672/0x010F4020) [7485*]:
    → "I hope we can plant lots of seeds, and people and beasty-weastymen can get along, like Fickie said."
  1: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0062 [0x21] END_EVENT
  3: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             5B 08 80 F8  FF FF 7F F8 FF FF 7F 74      [..........t
0070: 6C 6B 30 1C 09 80 00                              lk0....         
```

#### Opcodes

```
  0: 0x0064 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0073 [0x1C] WAIT(30* ticks)
  2: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      5B  08 80 F8 FF FF 7F F8 FF         [........
0080: FF 7F 70 61 73 30 53 F8  FF FF 7F F8 FF FF 7F 70  ..pas0S........p
0090: 61 73 30 00                                       as0.            
```

#### Opcodes

```
  0: 0x0077 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0086 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0094  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5E 69 64 6C  30 1C 0A 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x0094 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0099 [0x1C] WAIT(60* ticks)
  2: 0x009C [0x00] END_REQSTACK()
```
