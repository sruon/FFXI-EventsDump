# 17834313 - Yeggha Dolashi

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 492 bytes                |
| Total Events     | 8                        |
| References Count | 28                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [319](#event-319)     | 0x0001       |     47 |             11 |
| [327](#event-327)     | 0x0030       |      7 |              2 |
| [328](#event-328)     | 0x0037       |     33 |              9 |
| [2800](#event-2800)   | 0x0058       |     99 |             34 |
| [339](#event-339)     | 0x00BB       |     48 |             10 |
| [0](#event-0)         | 0x00EB       |      1 |              1 |
| [380](#event-380)     | 0x00EC       |     96 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x1F75      |        8053 |
|       2 | 0x1F76      |        8054 |
|       3 | 0x001E      |          30 |
|       4 | 0x0000      |           0 |
|       5 | 0x1D46      |        7494 |
|       6 | 0x1D47      |        7495 |
|       7 | 0x1D48      |        7496 |
|       8 | 0x1D49      |        7497 |
|       9 | 0x1D4A      |        7498 |
|      10 | 0x1D4B      |        7499 |
|      11 | 0x1D4C      |        7500 |
|      12 | 0x1D4D      |        7501 |
|      13 | 0x1D50      |        7504 |
|      14 | 0x1D51      |        7505 |
|      15 | 0x1D52      |        7506 |
|      16 | 0x1D53      |        7507 |
|      17 | 0x1F77      |        8055 |
|      18 | 0x1F78      |        8056 |
|      19 | 0x0001      |           1 |
|      20 | 0x2053      |        8275 |
|      21 | 0x2054      |        8276 |
|      22 | 0x0002      |           2 |
|      23 | 0x2057      |        8279 |
|      24 | 0x2058      |        8280 |
|      25 | 0x0003      |           3 |
|      26 | 0x2055      |        8277 |
|      27 | 0x2056      |        8278 |

## String References

- **7494**: This place is one where only a select few may engage in sacrrred battles.
- **7495**: Oh, you're here on behalf of the Peacekeeperrrs' Coalition?
- **7496**: That must have been quite the crrrawl.
- **7497**: As you experienced for yourself, the labyrrrinthine corridors are quite confounding, and have stymied many before you.
- **7498**: But making the jourrrney once makes subsequent visits all the easier, wouldn't you agree?
- **7499**: Along the way you must have come acrrross another gate with a symbol etched in stone.
- **7500**: Predictably, this gate is not like the otherrrs.
- **7501**: Passage is grrranted to specific individuals, and no one else.
- **7504**: These stories are best left for another time. I'm sure those who ordered you to confirrrm the status of the gates are waiting for word.
- **7505**: Me? There is no need for self-intrrroductions, as you've certainly heard my name before.
- **7506**: While you're at it, the Peacekeepers will be grrrateful for any assistance you can provide in keeping the road back safe for travel.
- **7507**: They must be waiting for you in the city prrroper. Hurry now.
- **8053**: This is the Watergarden Coliseum, where the Mummers' Coalition holds periodic rrraptor fights.
- **8054**: No raptor fights are currrently scheduled. You'll have to come back at a later date to satisfy your bloodlust.
- **8055**: What awe-inspiring rrrunic energy... Where have you been all this time!? We've been eagerrrly awaiting your arrival.
- **8056**: Prrreparations for the event are complete. When you're ready, just claw your way to the door at your rrrear.
- **8275**: You're after the Dashing Drrreamers?
- **8276**: Funny, that. They waltzed into the coliseum clutching a couple of barrrels from the warehouse nearby.
- **8277**: What on Vana'diel is going on in there? Firrrst Adoulin's famous duo sneaks in through the back, and now a Tarutaru hauls tail out of here drrragging another by his coattails?
- **8278**: He flailed about like a madman, screeching something about Svenja and the Orrrder of Janniston.
- **8279**: The Dashing Dreamers? Funny about that. The duo hauled a pairrr of squeaking barrels out the front door not two minutes ago.
- **8280**: Something about a carrrgo vessel and just desserts... I don't get paid enough to pay much attention.

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

### Event 319

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 21 00  ..........tlk2!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8053*)
    → "This is the Watergarden Coliseum, where the Mummers' Coalition holds periodic rrraptor fights."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8054*)
    → "No raptor fights are currrently scheduled. You'll have to come back at a later date to satisfy your bloodlust."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 327

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0030 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1E  F0 FF FF 7F 1C 03 80 66         ........f
0040: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 01  ..........tlk0..
0050: 80 23 1D 02 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0037 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003C [0x1C] WAIT(30* ticks)
  2: 0x003F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  3: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=8053*)
    → "This is the Watergarden Coliseum, where the Mummers' Coalition holds periodic rrraptor fights."
  4: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=8054*)
    → "No raptor fights are currrently scheduled. You'll have to come back at a later date to satisfy your bloodlust."
  6: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0056 [0x21] END_EVENT
  8: 0x0057 [0x00] END_REQSTACK()
```

### Event 2800

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 99 bytes |
| Instructions | 34       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          1E F0 FF FF 7F 42 6F 70          .....Bop
0060: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 02  f..........tlk0.
0070: 02 10 04 80 00 A6 00 1D  05 80 23 1D 06 80 23 1D  ..........#...#.
0080: 07 80 23 1D 08 80 23 1D  09 80 23 1D 0A 80 23 1D  ..#...#...#...#.
0090: 0B 80 23 1D 0C 80 23 1D  0D 80 23 1D 0E 80 23 1D  ..#...#...#...#.
00A0: 0F 80 23 01 AA 00 1D 10  80 23 66 00 80 F8 FF FF  ..#......#f.....
00B0: 7F F8 FF FF 7F 74 6C 6B  32 21 00                 .....tlk2!.     
```

#### Opcodes

```
  0: 0x0058 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x005F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0060 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  5: 0x006F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00A6
  6: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=7494*)
    → "This place is one where only a select few may engage in sacrrred battles."
  7: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7495*)
    → "Oh, you're here on behalf of the Peacekeeperrrs' Coalition?"
  9: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7496*)
    → "That must have been quite the crrrawl."
 11: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=7497*)
    → "As you experienced for yourself, the labyrrrinthine corridors are quite confounding, and have stymied many before you."
 13: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=7498*)
    → "But making the jourrrney once makes subsequent visits all the easier, wouldn't you agree?"
 15: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=7499*)
    → "Along the way you must have come acrrross another gate with a symbol etched in stone."
 17: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x008F [0x1D] PRINT_EVENT_MESSAGE(message_id=7500*)
    → "Predictably, this gate is not like the otherrrs."
 19: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7501*)
    → "Passage is grrranted to specific individuals, and no one else."
 21: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=7504*)
    → "These stories are best left for another time. I'm sure those who ordered you to confirrrm the status of the gates are waiting for word."
 23: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7505*)
    → "Me? There is no need for self-intrrroductions, as you've certainly heard my name before."
 25: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x009F [0x1D] PRINT_EVENT_MESSAGE(message_id=7506*)
    → "While you're at it, the Peacekeepers will be grrrateful for any assistance you can provide in keeping the road back safe for travel."
 27: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x00A3 [0x01] GOTO 0x00AA
 29: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7507*)
    → "They must be waiting for you in the city prrroper. Hurry now."
 30: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00AA:
 31: 0x00AA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 32: 0x00B9 [0x21] END_EVENT
 33: 0x00BA [0x00] END_REQSTACK()
```

### Event 339

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   1E F0 FF FF 7F             .....
00C0: 1C 03 80 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
00D0: 6B 30 1D 11 80 23 1D 12  80 23 66 00 80 F8 FF FF  k0...#...#f.....
00E0: 7F F8 FF FF 7F 74 6C 6B  32 21 00                 .....tlk2!.     
```

#### Opcodes

```
  0: 0x00BB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C0 [0x1C] WAIT(30* ticks)
  2: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  3: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8055*)
    → "What awe-inspiring rrrunic energy... Where have you been all this time!? We've been eagerrrly awaiting your arrival."
  4: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8056*)
    → "Prrreparations for the event are complete. When you're ready, just claw your way to the door at your rrrear."
  6: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00DA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  8: 0x00E9 [0x21] END_EVENT
  9: 0x00EA [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00EB [0x00] END_REQSTACK()
```

### Event 380

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 96 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      1E F0 FF FF              ....
00F0: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0100: 6B 30 02 02 10 13 80 80  15 01 1D 14 80 23 1D 15  k0...........#..
0110: 80 23 01 3B 01 02 02 10  16 80 80 28 01 1D 17 80  .#.;.......(....
0120: 23 1D 18 80 23 01 3B 01  02 02 10 19 80 80 3B 01  #...#.;.......;.
0130: 1D 1A 80 23 1D 1B 80 23  01 3B 01 66 00 80 F8 FF  ...#...#.;.f....
0140: FF 7F F8 FF FF 7F 74 6C  6B 32 21 00              ......tlk2!.    
```

#### Opcodes

```
  0: 0x00EC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00F2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00F3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0102 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0115
  5: 0x010A [0x1D] PRINT_EVENT_MESSAGE(message_id=8275*)
    → "You're after the Dashing Drrreamers?"
  6: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x010E [0x1D] PRINT_EVENT_MESSAGE(message_id=8276*)
    → "Funny, that. They waltzed into the coliseum clutching a couple of barrrels from the warehouse nearby."
  8: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0112 [0x01] GOTO 0x013B
 10: 0x0115 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0128
 11: 0x011D [0x1D] PRINT_EVENT_MESSAGE(message_id=8279*)
    → "The Dashing Dreamers? Funny about that. The duo hauled a pairrr of squeaking barrels out the front door not two minutes ago."
 12: 0x0120 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0121 [0x1D] PRINT_EVENT_MESSAGE(message_id=8280*)
    → "Something about a carrrgo vessel and just desserts... I don't get paid enough to pay much attention."
 14: 0x0124 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0125 [0x01] GOTO 0x013B
 16: 0x0128 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x013B
 17: 0x0130 [0x1D] PRINT_EVENT_MESSAGE(message_id=8277*)
    → "What on Vana'diel is going on in there? Firrrst Adoulin's famous duo sneaks in through the back, and now a Tarutaru hauls tail out of here drrragging another by his coattails?"
 18: 0x0133 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0134 [0x1D] PRINT_EVENT_MESSAGE(message_id=8278*)
    → "He flailed about like a madman, screeching something about Svenja and the Orrrder of Janniston."
 20: 0x0137 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0138 [0x01] GOTO 0x013B

SUBROUTINE_013B:
 22: 0x013B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
 23: 0x014A [0x21] END_EVENT
 24: 0x014B [0x00] END_REQSTACK()
```
