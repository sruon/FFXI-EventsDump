# 17842710 - Chya Mindorah

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Yahse Hunting Grounds (ID: 260) |
| Block Size       | 312 bytes                       |
| Total Events     | 5                               |
| References Count | 12                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2510](#event-2510)   | 0x0001       |     60 |             18 |
| [2511](#event-2511)   | 0x003D       |     48 |             12 |
| [2512](#event-2512)   | 0x006D       |     73 |             17 |
| [2513](#event-2513)   | 0x00B6       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0044      |          68 |
|       1 | 0x1D5E      |        7518 |
|       2 | 0x1D5F      |        7519 |
|       3 | 0x1D60      |        7520 |
|       4 | 0x1D61      |        7521 |
|       5 | 0x1D62      |        7522 |
|       6 | 0x1D63      |        7523 |
|       7 | 0x1D64      |        7524 |
|       8 | 0x1D65      |        7525 |
|       9 | 0x1D66      |        7526 |
|      10 | 0x00C9      |         201 |
|      11 | 0x0000      |           0 |

## String References

- **7518**: You're a pioneerrr--you can handle yourself out there, right? How about clipping the wings of that cursed chapuli for me?
- **7519**: Those chapuli chomp on the leaves of everrry last plant they find! What I need from you is to take out the big one--the head of the whole cloud.
- **7520**: I'd do it myself, but why sully my claws when someone purrrfectly capable of massacring the pest is right here?
- **7521**: It's masterrrfully good at staying out of sight, but attacking its swarm should call it out of hiding. Yeah, yeah, I know you don't wanna help, but think of it as a boon to the pioneering project.
- **7522**: Now get to it, before I leave scrrratch marks all over your arms!
- **7523**: You brought it, lock, stock, and barrel! Now that's the kind of furrrocity I can get behind! Now the chapuli shouldn't bother us for a while.
- **7524**: First we were concerned about the chapuli, but the further in we go the more we learn about the dangerrrs of Ulbuka. Nothing a good claw to the face can't handle, though.
- **7525**: What my viciousness can't handle, however, is the havoc these foul crrreatures wreak on the environment. This constant change doesn't bode well...
- **7526**: That's above my pay grrrade, though. You pioneers will have to handle the rest and claim your just reward. For now, this mere trifle will have to suffice.

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

### Event 2510

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
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=68*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7518*)
    → "You're a pioneerrr--you can handle yourself out there, right? How about clipping the wings of that cursed chapuli for me?"
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7519*)
    → "Those chapuli chomp on the leaves of everrry last plant they find! What I need from you is to take out the big one--the head of the whole cloud."
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7520*)
    → "I'd do it myself, but why sully my claws when someone purrrfectly capable of massacring the pest is right here?"
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7521*)
    → "It's masterrrfully good at staying out of sight, but attacking its swarm should call it out of hiding. Yeah, yeah, I know you don't wanna help, but think of it as a boon to the pioneering project."
 12: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7522*)
    → "Now get to it, before I leave scrrratch marks all over your arms!"
 14: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=68*
 16: 0x003B [0x21] END_EVENT
 17: 0x003C [0x00] END_REQSTACK()
```

### Event 2511

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         42 1E F0               B..
0040: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0050: 74 6C 62 30 1D 01 80 23  1D 04 80 23 66 00 80 F8  tlb0...#...#f...
0060: FF FF 7F F8 FF FF 7F 74  6C 62 31 21 00           .......tlb1!.   
```

#### Opcodes

```
  0: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0043 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0044 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=68*
  5: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7518*)
    → "You're a pioneerrr--you can handle yourself out there, right? How about clipping the wings of that cursed chapuli for me?"
  6: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7521*)
    → "It's masterrrfully good at staying out of sight, but attacking its swarm should call it out of hiding. Yeah, yeah, I know you don't wanna help, but think of it as a boon to the pioneering project."
  8: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=68*
 10: 0x006B [0x21] END_EVENT
 11: 0x006C [0x00] END_REQSTACK()
```

### Event 2512

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 73 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         42 1E F0               B..
0070: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0080: 74 6C 62 30 1D 06 80 23  1D 07 80 23 1D 08 80 23  tlb0...#...#...#
0090: 1D 09 80 23 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
00A0: 6C 62 31 45 0A 80 F0 FF  FF 7F F0 FF FF 7F 71 73  lb1E..........qs
00B0: 74 63 0B 80 21 00                                 tc..!.          
```

#### Opcodes

```
  0: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0074 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0075 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=68*
  5: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7523*)
    → "You brought it, lock, stock, and barrel! Now that's the kind of furrrocity I can get behind! Now the chapuli shouldn't bother us for a while."
  6: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7524*)
    → "First we were concerned about the chapuli, but the further in we go the more we learn about the dangerrrs of Ulbuka. Nothing a good claw to the face can't handle, though."
  8: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7525*)
    → "What my viciousness can't handle, however, is the havoc these foul crrreatures wreak on the environment. This constant change doesn't bode well..."
 10: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=7526*)
    → "That's above my pay grrrade, though. You pioneers will have to handle the rest and claim your just reward. For now, this mere trifle will have to suffice."
 12: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0094 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=68*
 14: 0x00A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x00B4 [0x21] END_EVENT
 16: 0x00B5 [0x00] END_REQSTACK()
```

### Event 2513

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   42 1E  F0 FF FF 7F 6F 70 66 00        B.....opf.
00C0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 30 1D 07 80  .........tlb0...
00D0: 23 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 31  #f..........tlb1
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00B6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00BC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00BD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00BE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=68*
  5: 0x00CD [0x1D] PRINT_EVENT_MESSAGE(message_id=7524*)
    → "First we were concerned about the chapuli, but the further in we go the more we learn about the dangerrrs of Ulbuka. Nothing a good claw to the face can't handle, though."
  6: 0x00D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=68*
  8: 0x00E0 [0x21] END_EVENT
  9: 0x00E1 [0x00] END_REQSTACK()
```
