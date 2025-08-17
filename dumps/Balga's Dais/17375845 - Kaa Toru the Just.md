# 17375845 - Kaa Toru the Just

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Balga's Dais (ID: 146) |
| Block Size       | 228 bytes              |
| Total Events     | 15                     |
| References Count | 18                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [32000](#event-32000)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0010       |      5 |              3 |
| [65535.3](#event-655353)   | 0x0015       |      5 |              3 |
| [65535.4](#event-655354)   | 0x001A       |      5 |              3 |
| [65535.5](#event-655355)   | 0x001F       |      5 |              3 |
| [65535.6](#event-655356)   | 0x0024       |      5 |              3 |
| [65535.7](#event-655357)   | 0x0029       |      5 |              3 |
| [32001](#event-32001)      | 0x002E       |      1 |              1 |
| [65535.8](#event-655358)   | 0x002F       |      5 |              3 |
| [65535.9](#event-655359)   | 0x0034       |      5 |              3 |
| [65535.10](#event-6553510) | 0x0039       |      5 |              3 |
| [65535.11](#event-6553511) | 0x003E       |      5 |              3 |
| [65535.12](#event-6553512) | 0x0043       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x5245      |       21061 |
|       2 | 0xFFFFD2D3  |  4294955731 |
|       3 | 0xFFFFEF54  |  4294963028 |
|       4 | 0x1DD9      |        7641 |
|       5 | 0x1DDA      |        7642 |
|       6 | 0x1DDB      |        7643 |
|       7 | 0x1DDC      |        7644 |
|       8 | 0x1DDD      |        7645 |
|       9 | 0x1DDE      |        7646 |
|      10 | 0x1DDF      |        7647 |
|      11 | 0x1DE0      |        7648 |
|      12 | 0x1DE1      |        7649 |
|      13 | 0x1DE2      |        7650 |
|      14 | 0x5208      |       21000 |
|      15 | 0xFFFF5C1D  |  4294925341 |
|      16 | 0xFFFFEE99  |  4294962841 |
|      17 | 0x0BE8      |        3048 |

## String References

- **7641**: I am Kaa Toru the Just.
- **7642**: Peace be. By grace of the Yagudo Holy One and the Star Sibyl of Windurst, I be holding Balga Contest here today.
- **7643**: In south corner, representing Yagudo, we be having blademaster Buu Xolo the Bloodfaced.
- **7644**: In north corner, representing Windurst, we be having <Player> the Unremarkable.
- **7645**: Outcome of this battle will be affecting the "Windurstian offerings to Oztroja" clause of Windurst-Oztroja peace treaty.
- **7646**: Combatants, swear that you will be fighting with honor, kyah!
- **7647**: Victor is <Player> of Windurst.
- **7648**: ...Listen to me, smoothskin. Take this $3 to Castle Oztroja. There you can exchange it for the $3, an oath that be concerning the Windurst offerings to Oztroja.
- **7649**: Got it, quawk? You be making your way to the top level of Castle Oztroja as fast as smoothskin two-legs can take you.
- **7650**: I now be closing the Balga Contest. Now flock off, kyah!

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=21.061*, Z=-11.565*, Y=-4.268*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1D 04 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7641*)
    → "I am Kaa Toru the Just."
  1: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1D 05 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7642*)
    → "Peace be. By grace of the Yagudo Holy One and the Star Sibyl of Windurst, I be holding Balga Contest here today."
  1: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1D 06 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7643*)
    → "In south corner, representing Yagudo, we be having blademaster Buu Xolo the Bloodfaced."
  1: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1D                 .
0020: 07 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7644*)
    → "In north corner, representing Windurst, we be having <Player> the Unremarkable."
  1: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1D 08 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7645*)
    → "Outcome of this battle will be affecting the "Windurstian offerings to Oztroja" clause of Windurst-Oztroja peace treaty."
  1: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 09 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7646*)
    → "Combatants, swear that you will be fighting with honor, kyah!"
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1D                 .
0030: 0A 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7647*)
    → "Victor is <Player> of Windurst."
  1: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0034  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             1D 0B 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=7648*)
    → "...Listen to me, smoothskin. Take this $3 to Castle Oztroja. There you can exchange it for the $3, an oath that be concerning the Windurst offerings to Oztroja."
  1: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1D 0C 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7649*)
    → "Got it, quawk? You be making your way to the top level of Castle Oztroja as fast as smoothskin two-legs can take you."
  1: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            1D 0D                ..
0040: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=7650*)
    → "I now be closing the Balga Contest. Now flock off, kyah!"
  1: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          37 0E 80 0F 80  10 80 11 80 00              7.........   
```

#### Opcodes

```
  0: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=21.000*, z=-41.955*, y=-4.455*, direction=267.9°*
  1: 0x004C [0x00] END_REQSTACK()
```
