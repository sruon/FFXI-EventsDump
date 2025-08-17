# 17797178 - Dieh Yamilsiah

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 188 bytes        |
| Total Events     | 5                |
| References Count | 10               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [231](#event-231)     | 0x0001       |     71 |             20 |
| [232](#event-232)     | 0x0048       |     13 |              7 |
| [233](#event-233)     | 0x0055       |     13 |              7 |
| [234](#event-234)     | 0x0062       |     13 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0090      |         144 |
|       1 | 0x003C      |          60 |
|       2 | 0x0000      |           0 |
|       3 | 0x1C64      |        7268 |
|       4 | 0x1C63      |        7267 |
|       5 | 0x1C66      |        7270 |
|       6 | 0x1C65      |        7269 |
|       7 | 0x1BEB      |        7147 |
|       8 | 0x1BF0      |        7152 |
|       9 | 0x1BED      |        7149 |

## String References

- **7147**: The ship bound for Selbina will arrrrive shortly.
- **7149**: The Selbina ferry will deparrrt soon! Passengers are to board the ship immediately!
- **7152**: This ship is headed for Selbina.
- **7267**: The ship bound for Selbina will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **7268**: The ship bound for Selbina is now [arriving/departing].
- **7269**: The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **7270**: The ship bound for Al Zahbi is now [arriving/departing].

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

### Event 231

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 71 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 03 04  10 02 10 15 04 10 00 80   ...............
0010: 15 02 10 01 80 02 05 10  02 80 00 33 00 02 02 10  ...........3....
0020: 02 80 00 2C 00 1D 03 80  23 01 30 00 1D 04 80 23  ...,....#.0....#
0030: 01 46 00 02 02 10 02 80  00 42 00 1D 05 80 23 01  .F.......B....#.
0040: 46 00 1D 06 80 23 21 00                           F....#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x03] Work_Zone[4] = Work_Zone[2]
  2: 0x000B [0x15] Work_Zone[4] /= 144*
  3: 0x0010 [0x15] Work_Zone[2] /= 60*
  4: 0x0015 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x0033
  5: 0x001D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002C
  6: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7268*)
    → "The ship bound for Selbina is now [arriving/departing]."
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x01] GOTO 0x0030
  9: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=7267*)
    → "The ship bound for Selbina will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
 10: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0030:
 11: 0x0030 [0x01] GOTO 0x0046
 12: 0x0033 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0042
 13: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=7270*)
    → "The ship bound for Al Zahbi is now [arriving/departing]."
 14: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003F [0x01] GOTO 0x0046
 16: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=7269*)
    → "The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
 17: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0046:
 18: 0x0046 [0x21] END_EVENT
 19: 0x0047 [0x00] END_REQSTACK()
```

### Event 232

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0050: 07 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7147*)
    → "The ship bound for Selbina will arrrrive shortly."
  4: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0053 [0x21] END_EVENT
  6: 0x0054 [0x00] END_REQSTACK()
```

### Event 233

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                1E F0 FF  FF 7F 6F 70 1D 08 80 23       .....op...#
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0055 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7152*)
    → "This ship is headed for Selbina."
  4: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0060 [0x21] END_EVENT
  6: 0x0061 [0x00] END_REQSTACK()
```

### Event 234

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1E F0 FF FF 7F 6F  70 1D 09 80 23 21 00       .....op...#!. 
```

#### Opcodes

```
  0: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0068 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=7149*)
    → "The Selbina ferry will deparrrt soon! Passengers are to board the ship immediately!"
  4: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x006D [0x21] END_EVENT
  6: 0x006E [0x00] END_REQSTACK()
```
