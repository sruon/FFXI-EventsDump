# 17793084 - Humilitie

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 200 bytes         |
| Total Events     | 5                 |
| References Count | 9                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [231](#event-231)     | 0x0001       |     41 |             12 |
| [232](#event-232)     | 0x002A       |     28 |              8 |
| [233](#event-233)     | 0x0046       |     28 |              8 |
| [234](#event-234)     | 0x0062       |     28 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0090      |         144 |
|       1 | 0x003C      |          60 |
|       2 | 0x0000      |           0 |
|       3 | 0x1C82      |        7298 |
|       4 | 0x1C81      |        7297 |
|       5 | 0x001E      |          30 |
|       6 | 0x1B70      |        7024 |
|       7 | 0x1B75      |        7029 |
|       8 | 0x1B72      |        7026 |

## String References

- **7024**: The ship to Mhaura's almost here.
- **7026**: Attention, passengers! The ship is about to depart. Please make haste!
- **7029**: This ship is bound for Mhaura.
- **7297**: The ship bound for Mhaura will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **7298**: The ship bound for Mhaura is now [arriving/departing]!

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
| Data Size    | 41 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 03 04  10 02 10 15 04 10 00 80   ...............
0010: 15 02 10 01 80 02 02 10  02 80 00 24 00 1D 03 80  ...........$....
0020: 23 01 28 00 1D 04 80 23  21 00                    #.(....#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x03] Work_Zone[4] = Work_Zone[2]
  2: 0x000B [0x15] Work_Zone[4] /= 144*
  3: 0x0010 [0x15] Work_Zone[2] /= 60*
  4: 0x0015 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0024
  5: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=7298*)
    → "The ship bound for Mhaura is now [arriving/departing]!"
  6: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0021 [0x01] GOTO 0x0028
  8: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7297*)
    → "The ship bound for Mhaura will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
  9: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0028:
 10: 0x0028 [0x21] END_EVENT
 11: 0x0029 [0x00] END_REQSTACK()
```

### Event 232

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                1E F0 FF FF 7F 6F            .....o
0030: 70 66 05 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  pf..........tlk0
0040: 1D 06 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x002A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0030 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0031 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=7024*)
    → "The ship to Mhaura's almost here."
  5: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0044 [0x21] END_EVENT
  7: 0x0045 [0x00] END_REQSTACK()
```

### Event 233

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1E F0  FF FF 7F 6F 70 66 05 80        .....opf..
0050: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 07 80 23  ........tlk0...#
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0046 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7029*)
    → "This ship is bound for Mhaura."
  5: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0060 [0x21] END_EVENT
  7: 0x0061 [0x00] END_REQSTACK()
```

### Event 234

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1E F0 FF FF 7F 6F  70 66 05 80 F8 FF FF 7F    .....opf......
0070: F8 FF FF 7F 74 6C 6B 30  1D 08 80 23 21 00        ....tlk0...#!.  
```

#### Opcodes

```
  0: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0068 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=7026*)
    → "Attention, passengers! The ship is about to depart. Please make haste!"
  5: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007C [0x21] END_EVENT
  7: 0x007D [0x00] END_REQSTACK()
```
