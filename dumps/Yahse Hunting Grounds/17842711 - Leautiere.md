# 17842711 - Leautiere

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Yahse Hunting Grounds (ID: 260) |
| Block Size       | 328 bytes                       |
| Total Events     | 5                               |
| References Count | 14                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2540](#event-2540)   | 0x0001       |     60 |             18 |
| [2541](#event-2541)   | 0x003D       |     44 |             10 |
| [2542](#event-2542)   | 0x0069       |     81 |             21 |
| [2543](#event-2543)   | 0x00BA       |     48 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1D6A      |        7530 |
|       2 | 0x1D6B      |        7531 |
|       3 | 0x1D6C      |        7532 |
|       4 | 0x1D6D      |        7533 |
|       5 | 0x1D6E      |        7534 |
|       6 | 0x1D6F      |        7535 |
|       7 | 0x1D70      |        7536 |
|       8 | 0x1D71      |        7537 |
|       9 | 0x1D72      |        7538 |
|      10 | 0x1D73      |        7539 |
|      11 | 0x1D74      |        7540 |
|      12 | 0x00C9      |         201 |
|      13 | 0x0000      |           0 |

## String References

- **7530**: One distinctive landmark of the Yahse Hunting Grounds is the Moh Gates, a grotto leading to the Morimar Basalt Fields.
- **7531**: Reports from our scouts have indicated the presence of several large fissures from which magma boils forth.
- **7532**: We have been charged with the exploration of this natural phenomenon, yet even our competency has some limits. If a pioneer were to lend [his/her] aid, however...
- **7533**: Should you be willing, I would request that you visit the gates, examine in great detail these fissures and the magma contained within, then report your findings back to me.
- **7534**: The lurid fiends found within the gates are of a calibre unmatched by those aboveground. Keep your wits about you and ensure your preparations are failsafe. The life you save may be your own.
- **7535**: Not even the horrors of the deeps can stop you! Pray tell, what have you discovered? A strange force within...hmmm, this corroborates the information that others have brought me.
- **7536**: To be frank, the gates are not the only location in Eastern Ulbuka where such mysterious energies reside.
- **7537**: Though such energies can be found throughout every region of Vana'diel, in Adoulin we have called them "ergon loci" since time immemorial. This term was invented by the geomancers, who boast an unparalleled harmony with nature.
- **7538**: This warmth that you felt goes beyond mere steam rising from magma. Indeed, you may have found one of these ergon loci. Still, this is beyond my area of expertise, so all I can proffer are simple theories.
- **7539**: Whether the locus is the magma itself or simply the whole area it runs through is not for me to say. This may be worthy of further research.
- **7540**: But you did not come here for a seminar on mystical puissance. Here. Your efforts deserve appropriate compensation.

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

### Event 2540

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F   B.....opf......
0010: F8 FF FF 7F 74 6C 62 30  1D 01 80 23 1D 02 80 23  ....tlb0...#...#
0020: 1D 03 80 23 1D 04 80 23  1D 05 80 23 66 00 80 F8  ...#...#...#f...
0030: FF FF 7F F8 FF FF 7F 74  6C 62 31 21 00           .......tlb1!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7530*)
    → "One distinctive landmark of the Yahse Hunting Grounds is the Moh Gates, a grotto leading to the Morimar Basalt Fields."
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7531*)
    → "Reports from our scouts have indicated the presence of several large fissures from which magma boils forth."
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7532*)
    → "We have been charged with the exploration of this natural phenomenon, yet even our competency has some limits. If a pioneer were to lend [his/her] aid, however..."
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7533*)
    → "Should you be willing, I would request that you visit the gates, examine in great detail these fissures and the magma contained within, then report your findings back to me."
 12: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7534*)
    → "The lurid fiends found within the gates are of a calibre unmatched by those aboveground. Keep your wits about you and ensure your preparations are failsafe. The life you save may be your own."
 14: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=20*
 16: 0x003B [0x21] END_EVENT
 17: 0x003C [0x00] END_REQSTACK()
```

### Event 2541

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         42 1E F0               B..
0040: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0050: 74 6C 62 30 1D 05 80 23  66 00 80 F8 FF FF 7F F8  tlb0...#f.......
0060: FF FF 7F 74 6C 62 31 21  00                       ...tlb1!.       
```

#### Opcodes

```
  0: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0044 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7534*)
    → "The lurid fiends found within the gates are of a calibre unmatched by those aboveground. Keep your wits about you and ensure your preparations are failsafe. The life you save may be your own."
  6: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0058 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=20*
  8: 0x0067 [0x21] END_EVENT
  9: 0x0068 [0x00] END_REQSTACK()
```

### Event 2542

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 81 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             42 1E F0 FF FF 7F 6F           B.....o
0070: 70 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 30  pf..........tlb0
0080: 1D 06 80 23 1D 07 80 23  1D 08 80 23 1D 09 80 23  ...#...#...#...#
0090: 1D 0A 80 23 1D 0B 80 23  66 00 80 F8 FF FF 7F F8  ...#...#f.......
00A0: FF FF 7F 74 6C 62 31 45  0C 80 F0 FF FF 7F F0 FF  ...tlb1E........
00B0: FF 7F 71 73 74 63 0D 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x0069 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0070 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0071 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7535*)
    → "Not even the horrors of the deeps can stop you! Pray tell, what have you discovered? A strange force within...hmmm, this corroborates the information that others have brought me."
  6: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7536*)
    → "To be frank, the gates are not the only location in Eastern Ulbuka where such mysterious energies reside."
  8: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7537*)
    → "Though such energies can be found throughout every region of Vana'diel, in Adoulin we have called them "ergon loci" since time immemorial. This term was invented by the geomancers, who boast an unparalleled harmony with nature."
 10: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7538*)
    → "This warmth that you felt goes beyond mere steam rising from magma. Indeed, you may have found one of these ergon loci. Still, this is beyond my area of expertise, so all I can proffer are simple theories."
 12: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=7539*)
    → "Whether the locus is the magma itself or simply the whole area it runs through is not for me to say. This may be worthy of further research."
 14: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=7540*)
    → "But you did not come here for a seminar on mystical puissance. Here. Your efforts deserve appropriate compensation."
 16: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0098 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=20*
 18: 0x00A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 19: 0x00B8 [0x21] END_EVENT
 20: 0x00B9 [0x00] END_REQSTACK()
```

### Event 2543

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BA   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                42 1E F0 FF FF 7F            B.....
00C0: 6F 70 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 62  opf..........tlb
00D0: 30 1D 09 80 23 1D 0A 80  23 66 00 80 F8 FF FF 7F  0...#...#f......
00E0: F8 FF FF 7F 74 6C 62 31  21 00                    ....tlb1!.      
```

#### Opcodes

```
  0: 0x00BA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00BB [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00C0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00C1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00C2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=20*
  5: 0x00D1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7538*)
    → "This warmth that you felt goes beyond mere steam rising from magma. Indeed, you may have found one of these ergon loci. Still, this is beyond my area of expertise, so all I can proffer are simple theories."
  6: 0x00D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7539*)
    → "Whether the locus is the magma itself or simply the whole area it runs through is not for me to say. This may be worthy of further research."
  8: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=20*
 10: 0x00E8 [0x21] END_EVENT
 11: 0x00E9 [0x00] END_REQSTACK()
```
