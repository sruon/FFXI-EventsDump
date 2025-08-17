# 17658625 - Mojuro-Nojuro

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 172 bytes                   |
| Total Events     | 2                           |
| References Count | 11                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [380](#event-380)     | 0x0001       |    103 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x2059      |        8281 |
|       2 | 0x205A      |        8282 |
|       3 | 0x205B      |        8283 |
|       4 | 0x0031      |          49 |
|       5 | 0x205C      |        8284 |
|       6 | 0x205D      |        8285 |
|       7 | 0x205E      |        8286 |
|       8 | 0x205F      |        8287 |
|       9 | 0x2060      |        8288 |
|      10 | 0x2061      |        8289 |

## String References

- **8281**: <Cough, hack>...
- **8282**: Ah...<wheeze>...forgive me. I seem to have come down with a case of the sniffle-wiffles.
- **8283**: Before I contracted this illness, I was quite the accomplished soldier myself. Let me share with you a bit of knowledge I acquired in my many battles againstaru the hordes.
- **8284**: Those nasty critters are far more intelligent than they look. Make swift work of a few, and their friends won'taru hesitate to call for reinforcements.
- **8285**: What's more, each one will prove more frightful-wightful than the last!
- **8286**: Fortunately, as tough as these bug-wuggers are, they also have vulnerabilities that can be exploited by the astute battler.
- **8287**: Strike them where it hurts, and they'll be left in a vastly weakened state. It would not be an understatementaru to call this the key to victory.
- **8288**: Also, you'll observe that the light of your visitant will glow all manner of pretty-wetty colors upon defeating a foe.
- **8289**: I've observed that the color depends on the...<cough>...killing-willing blow you...<cough>...strike... <Hack>...<wheeze>...This is my cue to shutaru up, it seems. Good luck in your...<hack>...battles!

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

### Event 380

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 103 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 65 68 6E 31 1D  01 80 23 53 F8 FF FF 7F  ...ehn1...#S....
0020: F8 FF FF 7F 65 68 6E 31  1D 02 80 23 1D 03 80 23  ....ehn1...#...#
0030: 66 04 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0040: 05 80 23 1D 06 80 23 1D  07 80 23 1D 08 80 23 1D  ..#...#...#...#.
0050: 09 80 23 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0060: 6B 31 1D 0A 80 23 21 00                           k1...#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn1" with entities [EventEntity, EventEntity], work=41*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8281*)
    → "<Cough, hack>..."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn1" with entities [EventEntity, EventEntity]
  7: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=8282*)
    → "Ah...<wheeze>...forgive me. I seem to have come down with a case of the sniffle-wiffles."
  8: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=8283*)
    → "Before I contracted this illness, I was quite the accomplished soldier myself. Let me share with you a bit of knowledge I acquired in my many battles againstaru the hordes."
 10: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 12: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8284*)
    → "Those nasty critters are far more intelligent than they look. Make swift work of a few, and their friends won'taru hesitate to call for reinforcements."
 13: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8285*)
    → "What's more, each one will prove more frightful-wightful than the last!"
 15: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8286*)
    → "Fortunately, as tough as these bug-wuggers are, they also have vulnerabilities that can be exploited by the astute battler."
 17: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8287*)
    → "Strike them where it hurts, and they'll be left in a vastly weakened state. It would not be an understatementaru to call this the key to victory."
 19: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=8288*)
    → "Also, you'll observe that the light of your visitant will glow all manner of pretty-wetty colors upon defeating a foe."
 21: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 23: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=8289*)
    → "I've observed that the color depends on the...<cough>...killing-willing blow you...<cough>...strike... <Hack>...<wheeze>...This is my cue to shutaru up, it seems. Good luck in your...<hack>...battles!"
 24: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0066 [0x21] END_EVENT
 26: 0x0067 [0x00] END_REQSTACK()
```
