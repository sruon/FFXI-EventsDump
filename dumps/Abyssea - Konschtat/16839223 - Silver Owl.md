# 16839223 - Silver Owl

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 304 bytes                    |
| Total Events     | 7                            |
| References Count | 17                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [256](#event-256)     | 0x0001       |     36 |             16 |
| [257](#event-257)     | 0x0025       |     20 |              8 |
| [258](#event-258)     | 0x0039       |     41 |             11 |
| [259](#event-259)     | 0x0062       |     11 |              5 |
| [260](#event-260)     | 0x006D       |     11 |              5 |
| [208](#event-208)     | 0x0078       |     69 |             30 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F21      |        7969 |
|       1 | 0x1F22      |        7970 |
|       2 | 0x1F23      |        7971 |
|       3 | 0x0640      |        1600 |
|       4 | 0x1F24      |        7972 |
|       5 | 0x1F25      |        7973 |
|       6 | 0x1F26      |        7974 |
|       7 | 0x1F27      |        7975 |
|       8 | 0x1F28      |        7976 |
|       9 | 0x1F29      |        7977 |
|      10 | 0x1F2A      |        7978 |
|      11 | 0x00C9      |         201 |
|      12 | 0x0000      |           0 |
|      13 | 0x1F2B      |        7979 |
|      14 | 0x1F20      |        7968 |
|      15 | 0x0001      |           1 |
|      16 | 0x0007      |           7 |

## String References

- **7968**: Losht shupplies of the Republic...they musht be found... But who can I trusht to find them...? <Mutter, mutter>...
- **7969**: You...they shpeak highly of you in theshe partsh... They call me Shilver Owl... Pray shpare a moment to lishen to the plea of thish old warrior...
- **7970**: You have sheen curioush cheshts shcattered acrosh the land... Shturdy boxshes called pyxshishesh...
- **7971**: Valuable shupplies they hold...armamentsh from the daysh when Bashtok shtill shtood tall... Before the fiendsh came and took everything from ush...even a humble guardshman'sh tongue...
- **7972**: ...But I digresh. Mosht valuable among these shpoilsh ish the $3. A raw material ushed in creating shellsh and other ammunition, thish ish...
- **7973**: If only we had a shupply of $3... I would craft a weapon... Yesh...a weapon that would shtrike fear in the heartsh of thoshe vile fiendsh...
- **7974**: Theshe days, it painsh me enough jusht to shpeak, let alone shwing a blade. Pleashe... Tell me that you will sheek out the pyxshishesh and retrieve the shupplies we need...
- **7975**: The $3... Shomeone musht find the $3...!
- **7976**: Do theshe old eyesh deshieve me? Is that $6 you hold!?
- **7977**: Friend...how can we ever repay you... You are our shavior...our lodeshtar in the darkesht night shky...
- **7978**: Thish may be nothing to you, but it ish all I poshesh... Pleashe...take it with my gratitude... Now, I musht begin work... Yesh...on the weapon that will shave our people!
- **7979**: The weapon...yesh...it is almost complete... Then...then the fiendsh will know the nightmaresh I have known! Eeheahaehaehaheehaah!

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

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 36 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 03 02 10 03 80 1D  04 80 23 1D 05 80 23 1D  .#........#...#.
0020: 06 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "You...they shpeak highly of you in theshe partsh... They call me Shilver Owl... Pray shpare a moment to lishen to the plea of thish old warrior..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "You have sheen curioush cheshts shcattered acrosh the land... Shturdy boxshes called pyxshishesh..."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "Valuable shupplies they hold...armamentsh from the daysh when Bashtok shtill shtood tall... Before the fiendsh came and took everything from ush...even a humble guardshman'sh tongue..."
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x03] Work_Zone[2] = 1600*
  8: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "...But I digresh. Mosht valuable among these shpoilsh ish the $3. A raw material ushed in creating shellsh and other ammunition, thish ish..."
  9: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "If only we had a shupply of $3... I would craft a weapon... Yesh...a weapon that would shtrike fear in the heartsh of thoshe vile fiendsh..."
 11: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "Theshe days, it painsh me enough jusht to shpeak, let alone shwing a blade. Pleashe... Tell me that you will sheek out the pyxshishesh and retrieve the shupplies we need..."
 13: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0023 [0x21] END_EVENT
 15: 0x0024 [0x00] END_REQSTACK()
```

### Event 257

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 20 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E F0 FF  FF 7F 03 02 10 03 80 1D       ...........
0030: 07 80 23 1D 06 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002A [0x03] Work_Zone[2] = 1600*
  2: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "The $3... Shomeone musht find the $3...!"
  3: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "Theshe days, it painsh me enough jusht to shpeak, let alone shwing a blade. Pleashe... Tell me that you will sheek out the pyxshishesh and retrieve the shupplies we need..."
  5: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0037 [0x21] END_EVENT
  7: 0x0038 [0x00] END_REQSTACK()
```

### Event 258

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 41 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1E F0 FF FF 7F 03 02           .......
0040: 10 03 80 1D 08 80 23 1D  09 80 23 1D 0A 80 23 45  ......#...#...#E
0050: 0B 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 0C 80  ..........qstc..
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003E [0x03] Work_Zone[2] = 1600*
  2: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "Do theshe old eyesh deshieve me? Is that $6 you hold!?"
  3: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "Friend...how can we ever repay you... You are our shavior...our lodeshtar in the darkesht night shky..."
  5: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7978*)
    → "Thish may be nothing to you, but it ish all I poshesh... Pleashe...take it with my gratitude... Now, I musht begin work... Yesh...on the weapon that will shave our people!"
  7: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0060 [0x21] END_EVENT
 10: 0x0061 [0x00] END_REQSTACK()
```

### Event 259

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1E F0 FF FF 7F 1D  0D 80 23 21 00             ........#!.   
```

#### Opcodes

```
  0: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7979*)
    → "The weapon...yesh...it is almost complete... Then...then the fiendsh will know the nightmaresh I have known! Eeheahaehaehaheehaah!"
  2: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x006B [0x21] END_EVENT
  4: 0x006C [0x00] END_REQSTACK()
```

### Event 260

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         1E F0 FF               ...
0070: FF 7F 1D 0E 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x006D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "Losht shupplies of the Republic...they musht be found... But who can I trusht to find them...? <Mutter, mutter>..."
  2: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0076 [0x21] END_EVENT
  4: 0x0077 [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 69 bytes |
| Instructions | 30       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          71 10 0F 80 71 11 00 00          q...q...
0080: 02 00 00 10 80 80 BB 00  1D 0E 80 23 1D 00 80 23  ...........#...#
0090: 1D 01 80 23 1D 02 80 23  1D 04 80 23 1D 05 80 23  ...#...#...#...#
00A0: 1D 06 80 23 1D 07 80 23  1D 08 80 23 1D 09 80 23  ...#...#...#...#
00B0: 1D 0A 80 23 1D 0D 80 23  01 BB 00 21 00           ...#...#...!.   
```

#### Opcodes

```
  0: 0x0078 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  1: 0x007C [0x71] USER_INPUT_HANDLER: Process numerical input A (work=ExtData[1]->WorkLocal[0])
  2: 0x0080 [0x02] IF !(ExtData[1]->WorkLocal[0] == 7*) GOTO 0x00BB
  3: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "Losht shupplies of the Republic...they musht be found... But who can I trusht to find them...? <Mutter, mutter>..."
  4: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "You...they shpeak highly of you in theshe partsh... They call me Shilver Owl... Pray shpare a moment to lishen to the plea of thish old warrior..."
  6: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "You have sheen curioush cheshts shcattered acrosh the land... Shturdy boxshes called pyxshishesh..."
  8: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "Valuable shupplies they hold...armamentsh from the daysh when Bashtok shtill shtood tall... Before the fiendsh came and took everything from ush...even a humble guardshman'sh tongue..."
 10: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "...But I digresh. Mosht valuable among these shpoilsh ish the $3. A raw material ushed in creating shellsh and other ammunition, thish ish..."
 12: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=7973*)
    → "If only we had a shupply of $3... I would craft a weapon... Yesh...a weapon that would shtrike fear in the heartsh of thoshe vile fiendsh..."
 14: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7974*)
    → "Theshe days, it painsh me enough jusht to shpeak, let alone shwing a blade. Pleashe... Tell me that you will sheek out the pyxshishesh and retrieve the shupplies we need..."
 16: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7975*)
    → "The $3... Shomeone musht find the $3...!"
 18: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "Do theshe old eyesh deshieve me? Is that $6 you hold!?"
 20: 0x00AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00AC [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "Friend...how can we ever repay you... You are our shavior...our lodeshtar in the darkesht night shky..."
 22: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7978*)
    → "Thish may be nothing to you, but it ish all I poshesh... Pleashe...take it with my gratitude... Now, I musht begin work... Yesh...on the weapon that will shave our people!"
 24: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7979*)
    → "The weapon...yesh...it is almost complete... Then...then the fiendsh will know the nightmaresh I have known! Eeheahaehaehaheehaah!"
 26: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00B8 [0x01] GOTO 0x00BB

SUBROUTINE_00BB:
 28: 0x00BB [0x21] END_EVENT
 29: 0x00BC [0x00] END_REQSTACK()
```
