# 17760287 - Yuhito-Kubhito

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 412 bytes               |
| Total Events     | 12                      |
| References Count | 22                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [447](#event-447)          | 0x0001       |    206 |             48 |
| [65535.1](#event-655351)   | 0x00CF       |      5 |              3 |
| [65535.2](#event-655352)   | 0x00D4       |      5 |              3 |
| [65535.3](#event-655353)   | 0x00D9       |      5 |              3 |
| [65535.4](#event-655354)   | 0x00DE       |      5 |              3 |
| [65535.5](#event-655355)   | 0x00E3       |      5 |              3 |
| [65535.6](#event-655356)   | 0x00E8       |      5 |              3 |
| [65535.7](#event-655357)   | 0x00ED       |      5 |              3 |
| [65535.8](#event-655358)   | 0x00F2       |      5 |              3 |
| [65535.9](#event-655359)   | 0x00F7       |      5 |              3 |
| [65535.10](#event-6553510) | 0x00FC       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2E4C      |       11852 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0xFFFFFFFC  |  4294967292 |
|       4 | 0x0003      |           3 |
|       5 | 0x2E5F      |       11871 |
|       6 | 0x2E60      |       11872 |
|       7 | 0x2E61      |       11873 |
|       8 | 0x2E62      |       11874 |
|       9 | 0x2E63      |       11875 |
|      10 | 0x2E64      |       11876 |
|      11 | 0x0002      |           2 |
|      12 | 0x2E4A      |       11850 |
|      13 | 0x2E4B      |       11851 |
|      14 | 0x2E4D      |       11853 |
|      15 | 0x2E4E      |       11854 |
|      16 | 0x2E4F      |       11855 |
|      17 | 0x2E50      |       11856 |
|      18 | 0x2E51      |       11857 |
|      19 | 0x2E52      |       11858 |
|      20 | 0x2E53      |       11859 |
|      21 | 0x2E54      |       11860 |

## String References

- **11850**: Wh-what? You don't want to see my chart of elemental correlations, do you? 'Cause if you do, well, I'm sorry, I don't know anything about such a thing.
- **11851**: Eeew... Well, if you're going to be so pushy about it... Here, but only because you're begging me to show it to you...
- **11852**: View the Chart of Elemental Correlations? [Yes./No.]
- **11853**: Well, that's your own choice. Just don't come crying to me when you try to put out a fire with powerful wind magic and end up creating a sea of flames instead!
- **11854**: Okay, okay...hold your horses. This is strictly between you and me, all rightaru?
- **11855**: Of course, you know about the prime elements, rightaru? They are the eight elements or energies that control the universe. This chart shows their interrelationships.
- **11856**: The six elements on the perimeter are in cyclical ascendancy over one another.
- **11857**: Or, putting it simply-wimply: Water dominates fire, fire dominates ice, ice dominates wind...
- **11858**: ...while wind dominates over earth, earth dominates lightning, and lightning dominates water.
- **11859**: The two elements in the center, light and darkness, are in direct opposition to each other.
- **11860**: And there you have it... But remember, this is our little secret, rightaru? Come back and ask to see it again whenever you need to jog your memory.
- **11871**: Oh, and one other thing: these elements are also closely connected to your health condition!
- **11872**: I can explain more about this if you're interested.
- **11873**: Hear him out? [Yes./No.]
- **11874**: Then listen up... Disease is to fire as paralysis is to ice, silence is to wind as petrification is to earth, and stun is to lightning as poison is to water.
- **11875**: Finally, there is charm, which is related to light, while blind, curse, and sleep are infused with the power of darkness.
- **11876**: What this all means is this: if your armor resists certain elements, then it will also help prevent the status ailments tied to those elements.

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

### Event 447

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 206 bytes |
| Instructions | 48        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    29 0B 1F 00 0F 01 02  1E F0 FF FF 7F 6F 70 29   )...........op)
0010: 0B 1F 00 0F 01 03 24 00  80 01 80 02 80 25 02 00  ......$......%..
0020: 10 02 80 00 B4 00 03 01  10 01 80 29 0B 1F 00 0F  ...........)....
0030: 01 05 9C 00 00 02 00 00  01 80 00 45 00 8D 03 80  ...........E....
0040: 01 80 01 4A 00 8D 03 80  04 80 29 0B 1F 00 0F 01  ...J......).....
0050: 06 29 0B 1F 00 0F 01 07  29 0B 1F 00 0F 01 08 29  .)......)......)
0060: 0B 1F 00 0F 01 09 29 0B  1F 00 0F 01 0A 1D 05 80  ......).........
0070: 23 8A 1D 06 80 23 24 07  80 01 80 02 80 25 02 00  #....#$......%..
0080: 10 02 80 00 9A 00 03 01  10 01 80 1D 08 80 23 1D  ..............#.
0090: 09 80 23 1D 0A 80 23 01  AA 00 02 00 10 01 80 00  ..#...#.........
00A0: AA 00 03 01 10 0B 80 01  AA 00 29 0B 1F 00 0F 01  ..........).....
00B0: 0B 01 CB 00 02 00 10 01  80 00 CB 00 03 01 10 0B  ................
00C0: 80 29 0B 1F 00 0F 01 04  01 CB 00 20 00 21 00     .)......... .!. 
```

#### Opcodes

```
  0: 0x0001 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x02)
  1: 0x0008 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x03)
  5: 0x0016 [0x24] CREATE_DIALOG(message_id=11852*, default_option=1*, option_flags=0*)
    → "View the Chart of Elemental Correlations? [Yes./No.]"
  6: 0x001D [0x25] WAIT_DIALOG_SELECT()
  7: 0x001E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B4
  8: 0x0026 [0x03] Work_Zone[1] = 1*
  9: 0x002B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x05)
 10: 0x0032 [0x9C] STORE_CLIENT_LANGUAGE_ID(result=0x00)
 11: 0x0035 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0045
 12: 0x003D [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967292*, properties=1*)
 13: 0x0042 [0x01] GOTO 0x004A
 14: 0x0045 [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967292*, properties=3*)

SUBROUTINE_004A:
 15: 0x004A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x06)
 16: 0x0051 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x07)
 17: 0x0058 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x08)
 18: 0x005F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x09)
 19: 0x0066 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x0A)
 20: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=11871*)
    → "Oh, and one other thing: these elements are also closely connected to your health condition!"
 21: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0071 [0x8A] CLOSE_MAP()
 23: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=11872*)
    → "I can explain more about this if you're interested."
 24: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0076 [0x24] CREATE_DIALOG(message_id=11873*, default_option=1*, option_flags=0*)
    → "Hear him out? [Yes./No.]"
 26: 0x007D [0x25] WAIT_DIALOG_SELECT()
 27: 0x007E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009A
 28: 0x0086 [0x03] Work_Zone[1] = 1*
 29: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=11874*)
    → "Then listen up... Disease is to fire as paralysis is to ice, silence is to wind as petrification is to earth, and stun is to lightning as poison is to water."
 30: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=11875*)
    → "Finally, there is charm, which is related to light, while blind, curse, and sleep are infused with the power of darkness."
 32: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=11876*)
    → "What this all means is this: if your armor resists certain elements, then it will also help prevent the status ailments tied to those elements."
 34: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0097 [0x01] GOTO 0x00AA
 36: 0x009A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00AA
 37: 0x00A2 [0x03] Work_Zone[1] = 2*
 38: 0x00A7 [0x01] GOTO 0x00AA

SUBROUTINE_00AA:
 39: 0x00AA [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x0B)
 40: 0x00B1 [0x01] GOTO 0x00CB
 41: 0x00B4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00CB
 42: 0x00BC [0x03] Work_Zone[1] = 2*
 43: 0x00C1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Yuhito-Kubhito (ID: 17760287/0x010F001F), tag_num=0x04)
 44: 0x00C8 [0x01] GOTO 0x00CB

SUBROUTINE_00CB:
 45: 0x00CB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 46: 0x00CD [0x21] END_EVENT
 47: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CF  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               1D                 .
00D0: 0C 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=11850*)
    → "Wh-what? You don't want to see my chart of elemental correlations, do you? 'Cause if you do, well, I'm sorry, I don't know anything about such a thing."
  1: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             1D 0D 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=11851*)
    → "Eeew... Well, if you're going to be so pushy about it... Here, but only because you're begging me to show it to you..."
  1: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D9  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             1D 0E 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=11853*)
    → "Well, that's your own choice. Just don't come crying to me when you try to put out a fire with powerful wind magic and end up creating a sea of flames instead!"
  1: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DE  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            1D 0F                ..
00E0: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=11854*)
    → "Okay, okay...hold your horses. This is strictly between you and me, all rightaru?"
  1: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E3  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          1D 10 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=11855*)
    → "Of course, you know about the prime elements, rightaru? They are the eight elements or energies that control the universe. This chart shows their interrelationships."
  1: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00E7 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E8  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          1D 11 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x00E8 [0x1D] PRINT_EVENT_MESSAGE(message_id=11856*)
    → "The six elements on the perimeter are in cyclical ascendancy over one another."
  1: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00EC [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00ED  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         1D 12 80               ...
00F0: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x00ED [0x1D] PRINT_EVENT_MESSAGE(message_id=11857*)
    → "Or, putting it simply-wimply: Water dominates fire, fire dominates ice, ice dominates wind..."
  1: 0x00F0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F2  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       1D 13 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x00F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11858*)
    → "...while wind dominates over earth, earth dominates lightning, and lightning dominates water."
  1: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F7  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      1D  14 80 23 00                     ...#.    
```

#### Opcodes

```
  0: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=11859*)
    → "The two elements in the center, light and darkness, are in direct opposition to each other."
  1: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FC  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      1D 15 80 23              ...#
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00FC [0x1D] PRINT_EVENT_MESSAGE(message_id=11860*)
    → "And there you have it... But remember, this is our little secret, rightaru? Come back and ask to see it again whenever you need to jog your memory."
  1: 0x00FF [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0100 [0x00] END_REQSTACK()
```
